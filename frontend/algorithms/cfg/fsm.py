import pygraphviz as pgv
from typing import List, Dict

from .cfg import *


class FSM(pgv.AGraph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.graph_attr["rankdir"] = "TB"
        self.nodeToBB: Dict[str, str] = {}
        self.bbToNodes: Dict[str, List[str]] = {}
        self.bbs: List[str] = []
        self.bbToFlows: Dict[str, List[str]] = {}

        # this is the idle state
        self._initialState: pgv.Node = None
        self._finalState: pgv.Node = None

    def addBB(self, bb: pgv.Node, isStart: bool = False, isFinish: bool = False):
        bbName = bb.name
        self.bbs.append(bbName)
        self.bbToNodes[bbName] = []
        latency = int(bb.attr["latency"])

        # TODO: if II is not None, then we need a latency-insensitive region
        prevNode = None
        for _ in range(latency):
            nodeName = f"s{len(self.nodes())}"
            self.add_node(nodeName)
            self.nodeToBB[nodeName] = bbName
            self.bbToNodes[bbName].append(nodeName)

            # add the edge to the previous node
            if prevNode is not None:
                self.add_edge(prevNode, nodeName)
            prevNode = nodeName

        if isStart:
            assert self._initialState is None, "Multiple initial states"
            self._initialState = self.get_node(self.bbToNodes[bbName][0])

        if isFinish:
            assert self._finalState is None, "Multiple final states"
            self._finalState = self.get_node(self.bbToNodes[bbName][-1])

    def getIdleState(self) -> pgv.Node:
        return self._initialState

    def getFinalState(self) -> pgv.Node:
        return self._finalState

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
        fsm.addBB(node, isStart=CFGraph.isStart(node), isFinish=CFGraph.isFinish(node))
    # Add flows between basic blocks in FSM
    for edge in cfgraph.edges():
        src = edge[0]
        dst = edge[1]
        fsm.addFlow(src, dst)
    return fsm
