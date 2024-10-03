import pygraphviz as pgv
from typing import List, Dict
import math

from ...modules import *


class CFGraph(pgv.AGraph):

    def getLatency(self, node: pgv.Node):
        return int(node.attr["latency"])

    def getII(self, node: pgv.Node):
        if "II" not in node.attr:
            return None
        if node.attr["II"] == "None":
            return None
        return node.attr["II"]

    def addBB(self, name: str, latency: int, II: int = None, isStart: bool = False):
        self.add_node(
            name,
            shape="box",
            latency=latency,
            II=II,
            isStart="true" if isStart else "false",
        )

    def addFlow(self, src: str, dst: str):
        self.add_edge(src, dst)


class FSM(pgv.AGraph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.graph_attr["rankdir"] = "TB"
        self.nodeToBB: Dict[str, str] = {}
        self.bbToNodes: Dict[str, List[str]] = {}
        self.bbs: List[str] = []
        self.bbToFlows: Dict[str, List[str]] = {}
        self.initialState: pgv.Node = None

    def addBB(self, bb: pgv.Node, isStart: bool = False):
        bbName = bb.name
        self.bbs.append(bbName)
        self.bbToNodes[bbName] = []
        latency = int(bb.attr["latency"])

        # TODO: if II is not None, then we need a latency-insensitive region
        prevNode = None
        for i in range(latency):
            nodeName = f"s{len(self.nodes())}"
            self.add_node(nodeName)
            self.nodeToBB[nodeName] = bbName
            self.bbToNodes[bbName].append(nodeName)

            # add the edge to the previous node
            if prevNode is not None:
                self.add_edge(prevNode, nodeName)
            prevNode = nodeName

        if isStart:
            assert self.initialState is None, "Multiple initial states"
            self.initialState = self.get_node(self.bbToNodes[bbName][0])

    def addFlow(self, src: pgv.Node, dst: pgv.Node):
        """
        Let us assume for now that the last flow added is the default flow
        For each other flow, we need to add a control signal
        They are matched in the order they are added
        """
        srcName = src.name
        dstName = dst.name
        self.add_edge(self.bbToNodes[srcName][-1], self.bbToNodes[dstName][0])
        if srcName not in self.bbToFlows:
            self.bbToFlows[srcName] = []
        self.bbToFlows[srcName].append(dstName)

    def numSuccessors(self, bb: str) -> int:
        return len(self.bbToFlows.get(bb, []))

    def getControlSignalAtBB(self, bb: str, idx: int) -> VarNode:
        return VarNode(f"{bb}_ctrl_in{idx}")

    def getControlSignalAtNode(self, node: pgv.Node, idx: int) -> VarNode:
        node = self.get_node(node) if isinstance(node, str) else node
        bb = self.nodeToBB[node.name]
        return self.getControlSignalAtBB(bb, idx)

    def getParamAtNode(self, node: pgv.Node) -> VarNode:
        node = self.get_node(node) if isinstance(node, str) else node
        return VarNode(f"{node.name}_label")


def cfg2fsm(cfgraph: CFGraph) -> FSM:
    fsm = FSM(strict=False, directed=True)
    # Add basic blocks to FSM
    for node in cfgraph.nodes():
        fsm.addBB(node, isStart=node.attr["isStart"] == "true")
    # Add flows between basic blocks in FSM
    for edge in cfgraph.edges():
        src = edge[0]
        dst = edge[1]
        fsm.addFlow(src, dst)
    return fsm


def fsm2module(fsm: FSM) -> Module:
    module = Module()

    assert len(fsm.nodes()) > 0, "FSM is empty"
    width: int = math.ceil(math.log2(len(fsm.nodes())))

    nextStateNode = VarNode("next_state")
    currStateNode = VarNode("curr_state")
    module.addPort(RegPort(nextStateNode, BasicRange(width)))
    module.addPort(WirePort(currStateNode, BasicRange(width)))

    for i, node in enumerate(fsm.nodes()):
        # we define each state as a parameter
        paramNode = fsm.getParamAtNode(node)
        module.addPort(ParameterPort(paramNode, BasicRange(width)))
        module.addAssignment(Assignment(paramNode, ConstantNode(f"3'd{i}")))

        # for each parameter, we need to output a control signal, which is the comparison between the current state and the parameter
        compNode = OPNode("==", OPType.BINARY_EQ, currStateNode, paramNode)
        outName = node.name + "_ctrl_out"
        outNode = VarNode(outName)
        module.addPort(OutputPort(outNode, BasicRange(1)))
        module.addAssignment(Assignment(outNode, compNode))

    # for each bb with more than one successor, we need an input port
    for bb in fsm.bbs:
        for i in range(fsm.numSuccessors(bb) - 1):
            inputNode = fsm.getControlSignalAtBB(bb, i)
            module.addPort(InputPort(inputNode, BasicRange(1)))

    # for each state transition, we need to update the next state
    event = OPNode("always", OPType.EVENT_ALWAYS, OPNode("*", OPType.EVENT_COMB))
    assignment = CaseAssignment(nextStateNode, currStateNode, event=event)
    for i, node in enumerate(fsm.nodes()):
        currParamNode = fsm.getParamAtNode(node)
        if len(fsm.successors(node)) == 0:
            continue
        elif len(fsm.successors(node)) == 1:
            succ = fsm.successors(node)[0]
            nextParamNode = fsm.getParamAtNode(succ)
            nextStateAssignment = Assignment(
                nextStateNode, nextParamNode, targetType=PortType.REG, isBlocking=True
            )
        else:
            conditionalAssignment = ConditionalAssignment(nextStateNode)
            for j, succ in enumerate(fsm.successors(node)[:-1]):
                controlNode = fsm.getControlSignalAtNode(succ, j)
                nextParamNode = fsm.getParamAtNode(succ)
                conditionalAssignment.addBranch(
                    controlNode,
                    Assignment(
                        nextStateNode,
                        nextParamNode,
                        targetType=PortType.REG,
                        isBlocking=True,
                    ),
                )
            # add a default case to the conditional assignment
            nextParamNode = fsm.getParamAtNode(fsm.successors(node)[-1])
            conditionalAssignment.addBranch(
                None,
                Assignment(
                    nextStateNode,
                    nextParamNode,
                    targetType=PortType.REG,
                    isBlocking=True,
                ),
            )
            nextStateAssignment = conditionalAssignment
        assignment.addCase(currParamNode, nextStateAssignment)
    # add a default case to the current state
    assert fsm.initialState is not None, "FSM has no initial state"
    initialStateNode = VarNode(fsm.initialState.name + "_label")
    assignment.addCase(
        None,
        Assignment(
            nextStateNode, initialStateNode, targetType=PortType.REG, isBlocking=True
        ),
    )

    # add the case assignment to the module
    module.addAssignment(assignment)

    return module
