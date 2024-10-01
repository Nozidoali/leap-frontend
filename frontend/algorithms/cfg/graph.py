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

    def addBB(self, name: str, latency: int, II: int = None):
        self.add_node(name, shape="box", latency=latency, II=II)

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

    def addBB(self, bb: pgv.Node):
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

    def addFlow(self, src: pgv.Node, dst: pgv.Node):
        srcName = src.name
        dstName = dst.name
        self.add_edge(self.bbToNodes[srcName][-1], self.bbToNodes[dstName][0])
        if srcName not in self.bbToFlows:
            self.bbToFlows[srcName] = []
        self.bbToFlows[srcName].append(dstName)

    def numSuccessors(self, bb: str) -> int:
        return len(self.bbToFlows.get(bb, []))


def cfg2fsm(cfgraph: CFGraph) -> FSM:
    fsm = FSM(strict=False, directed=True)
    # Add basic blocks to FSM
    for node in cfgraph.nodes():
        fsm.addBB(node)
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

    # we define each state as a parameter
    for i, node in enumerate(fsm.nodes()):
        paramNode = VarNode(node.name + "_label")
        module.addPort(ParameterPort(paramNode, BasicRange(width)))
        module.addAssignment(Assignment(paramNode, ConstantNode(f"3'd{i}")))

    # for each parameter, we need to output a control signal, which is the comparison between the current state and the parameter
    for i, node in enumerate(fsm.nodes()):
        paramNode = VarNode(node.name + "_label")
        compNode = OPNode("==", OPType.BINARY_EQ, currStateNode, paramNode)
        outName = node.name + "_ctrl_out"
        outNode = VarNode(outName)
        module.addPort(OutputPort(outNode, BasicRange(1)))
        module.addAssignment(Assignment(outNode, compNode))

    # for each bb with more than one successor, we need an input port
    for bb in fsm.bbs:
        if fsm.numSuccessors(bb) > 1:
            inputNode = VarNode(f"{bb}_ctrl_in")
            module.addPort(InputPort(inputNode, BasicRange(1)))

    return module
