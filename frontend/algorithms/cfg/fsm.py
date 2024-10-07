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

        # handle loops and pipeline stages
        self.__loops: List[pgv.Edge] = []
        self.__loopToBounds: Dict[pgv.Edge, int] = {}
        self.__loopToII: Dict[pgv.Edge, int] = {}

        self.__loopStart: Dict[pgv.Node, pgv.Edge] = {}

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

    def addFlow(
        self,
        src: pgv.Node,
        dst: pgv.Node,
        isLoop: bool = False,
        loopBound: int = None,
        loopII: int = None,
    ):
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

        u = self.get_node(self.bbToNodes[srcName][-1])
        v = self.get_node(self.bbToNodes[dstName][0])
        edge = self.get_edge(u, v)
        # handle loops
        if isLoop:
            self.__loops.append(edge)
            self.__loopToBounds[edge] = loopBound
            self.__loopToII[edge] = loopII

            self.__loopStart[v] = edge

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

    def getLoops(self) -> List[pgv.Edge]:
        return self.__loops

    def getLoopBound(self, edge: pgv.Edge) -> int:
        return self.__loopToBounds[edge]

    def getLoopII(self, edge: pgv.Edge) -> int:
        return self.__loopToII[edge]

    def getLoopStart(self, node: pgv.Node) -> pgv.Edge:
        if node not in self.__loopStart:
            return None
        return self.__loopStart[node]


def cfg2fsm(cfgraph: CFGraph) -> FSM:
    fsm = FSM(strict=False, directed=True)
    # Add basic blocks to FSM
    for node in cfgraph.nodes():
        fsm.addBB(node, isStart=CFGraph.isStart(node), isFinish=CFGraph.isFinish(node))
    # Add flows between basic blocks in FSM
    for edge in cfgraph.edges():
        src = edge[0]
        dst = edge[1]
        fsm.addFlow(
            src,
            dst,
            isLoop=CFGraph.isLoop(edge),
            loopBound=CFGraph.getLoopBound(edge),
            loopII=CFGraph.getLoopII(edge),
        )
    return fsm


import imageio
from io import BytesIO


def _renderFrame(
    fsm: FSM, stateEnables: Dict[pgv.Node, bool], loopFiredCount: Dict[pgv.Edge, int]
) -> BytesIO:
    # render the current state
    for node in fsm.nodes():
        if stateEnables[node]:
            fsm.get_node(node).attr["color"] = "blue"
            fsm.get_node(node).attr["style"] = "filled"
            # font color white
            fsm.get_node(node).attr["fontcolor"] = "white"
        else:
            fsm.get_node(node).attr["color"] = "white"
            fsm.get_node(node).attr["style"] = "filled"
            # font color black
            fsm.get_node(node).attr["fontcolor"] = "black"

    # render the current edge
    for edge in fsm.edges():
        if edge in fsm.getLoops():
            # label the remaining iterations
            edge.attr["label"] = f"{fsm.getLoopBound(edge) - loopFiredCount[edge]}"
    img_data = fsm.draw(format="png")
    # Store the image in memory using BytesIO
    img_io = BytesIO(img_data)
    return img_io


def _getNextState(
    fsm: FSM,
    stateEnables: Dict[pgv.Node, bool],
    loopFiredCount: Dict[pgv.Edge, int],
    loopIIcounters: Dict[pgv.Edge, int],
    loopEnabled: Dict[pgv.Edge, bool],
    loopFinished: Dict[pgv.Edge, bool],
) -> Dict[pgv.Node, bool]:
    nextStateEnables = {node: False for node in fsm.nodes()}

    def onEnable(node: pgv.Node):
        nextStateEnables[node] = True
        loop = fsm.getLoopStart(node)
        if loop is not None:
            loopEnabled[loop] = True
            loopFiredCount[loop] = 1  # we just fired one iteration

    def onBranch(node: pgv.Node):
        for succ in fsm.successors(node):
            edge = fsm.get_edge(node, succ)
            if edge in fsm.getLoops():
                assert loopEnabled[edge], "Loop should be enabled"
                if loopFiredCount[edge] < fsm.getLoopBound(edge):
                    onEnable(succ)
                return
            else:
                onEnable(succ)
                return

    # II simulation
    for loop in fsm.getLoops():
        if loopEnabled[loop]:
            loopIIcounters[loop] += 1
            if loopIIcounters[loop] == fsm.getLoopII(loop):
                loopIIcounters[loop] = 0
                # fires another token
                if loopFiredCount[loop] < fsm.getLoopBound(loop):
                    loopFiredCount[loop] += 1
                    nextStateEnables[fsm.get_node(loop[1])] = True

    # state simulation
    for node in fsm.nodes():
        if stateEnables[node]:
            if len(fsm.successors(node)) > 1:
                onBranch(node)
            else:
                succ = fsm.successors(node)[0]
                onEnable(succ)

    return nextStateEnables


def fsmToGIF(fsm: FSM, filename: str):

    images: List[BytesIO] = []

    fsm.layout(prog="dot")

    # start the simulation from the initial state
    stateEnables = {node: False for node in fsm.nodes()}
    stateEnables[fsm.getIdleState()] = True

    loopFiredCount = {edge: 0 for edge in fsm.getLoops()}

    loopIIcounters = {edge: 0 for edge in fsm.getLoops()}
    loopEnabled = {edge: False for edge in fsm.getLoops()}
    loopFinished = {edge: False for edge in fsm.getLoops()}

    for cycle in range(100):
        print(f"Cycle {cycle}", end="\r")
        img_io = _renderFrame(fsm, stateEnables, loopFiredCount)
        images.append(imageio.imread(img_io))  # Read the image from BytesIO object
        if stateEnables[fsm.getFinalState()]:
            break

        # get the next state
        stateEnables = _getNextState(
            fsm, stateEnables, loopFiredCount, loopIIcounters, loopEnabled, loopFinished
        )

    # Save as GIF
    imageio.mimsave(filename, images, duration=0.5)  # Duration in seconds per frame
