from typing import List, Dict, Any
import pygraphviz as pgv
import tqdm

from ..cfg import *


class FSMSimulator:
    def __init__(self, fsm: FSM) -> None:
        super().__init__()
        # fsm state enabled
        self._fsm: FSM = fsm
        self._fsm_state_enabled: Dict[pgv.Node, bool] = {}
        self._fsm_state_enabled_reg: Dict[pgv.Node, bool] = {}

        self._fsm_node_dirty_attr: Dict[pgv.Node, Dict[str, Any]] = {}

        self._loops: List[pgv.Edge] = []

        # detach the loop from the fsm
        self._loopEntrance: Dict[pgv.Edge, pgv.Node] = {}
        self._loopWait: Dict[pgv.Edge, pgv.Node] = {}
        self._loopExit: Dict[pgv.Edge, pgv.Node] = {}

        # some precalculated values
        self._wait_states: Dict[pgv.Node, pgv.Node] = {}

        # some precalculated values
        self._regular_edges: List[pgv.Edge] = []
        self._regular_nodes: List[pgv.Node] = []
        self._modifyFSM()
        self._bindFSM()

    def _bindFSM(self) -> None:

        # during initialization, we deligate the FSM states to the regular states
        for node in self._fsm.nodes():
            if node != self._fsm.getIdleState():
                self._dehighlightNode(node)
            else:
                self._highlightNode(node)

        self._catagorizeEdges()
        # for each loop, we need to find the start node
        self._fsm_state_enabled = {node: False for node in self._regular_nodes}

        assert self._fsm.getIdleState() in self._fsm_state_enabled
        self._fsm_state_enabled[self._fsm.getIdleState()] = True
        # layout
        self._fsm.layout(prog="dot")

    def _renderFSM(self) -> BytesIO:
        # clean up the dirty attributes
        for node, attrs in self._fsm_node_dirty_attr.items():
            for key, value in attrs.items():
                # set the attribute
                self._fsm.get_node(node).attr[key] = value
        # remove all dirty attributes
        self._fsm_node_dirty_attr = {}

        img_data = self._fsm.draw(format="png")
        img_io = BytesIO(img_data)
        return img_io

    def _highlightNode(self, node: pgv.Node) -> None:
        self._fsm_node_dirty_attr[node] = {
            "color": "red",
            "style": "filled",
            "fontcolor": "white",
        }

    def _dehighlightNode(self, node: pgv.Node) -> None:
        self._fsm_node_dirty_attr[node] = {
            "color": "white",
            "style": "filled",
            "fontcolor": "black",
        }

    def isWaitState(self, node: pgv.Node) -> bool:
        return node in self._wait_states

    def getWaitState(self, loop: pgv.Edge) -> pgv.Node:
        return self._loopWait[loop]

    def getExitState(self, loop: pgv.Edge) -> pgv.Node:
        return self._loopExit[loop]

    def _catagorizeEdges(self) -> None:
        self._regular_edges = []
        self._regular_nodes = []

        # we run a BFS from the idle state
        # all states that are reachable from the idle state and is not a wait state is a regular state
        stack: List[pgv.Node] = [self._fsm.getIdleState()]

        while stack:
            node = stack.pop()
            self._regular_nodes.append(node)
            if self.isWaitState(node):
                # we skip the wait state
                # but add the exit state to the stack
                loop = self._wait_states[node]
                stack.append(self._loopExit[loop])
                continue
            for succ in self._fsm.successors(node):
                stack.append(succ)
                self._regular_edges.append(self._fsm.get_edge(node, succ))

        # for debugging
        # for edge in self._regular_edges:
        #     print(edge)

    def _checkExitCondition(self) -> bool:
        # check the exit condition
        if not self._fsm_stall and not self._reset:
            if self._fsm_state_enabled[self._fsm.getFinalState()]:
                return True
        return False

    def stateTransition(self, stateFrom: pgv.Node, stateTo: pgv.Node) -> None:
        self._fsm_state_enabled_reg[stateFrom] = False
        self._fsm_state_enabled_reg[stateTo] = True

    def _propagateFSMstates(self) -> bool:
        # regular nodes
        self._fsm_state_enabled_reg: Dict[pgv.Node, bool] = {}
        for edge in self._regular_edges:
            if self._fsm_state_enabled[edge[0]]:
                self.stateTransition(edge[0], edge[1])

    def step(self) -> bool:
        """
        Put all blocking assignments here
        """
        # check the exit condition
        if self._checkExitCondition():
            return True

        # propagate the FSM states
        self._propagateFSMstates()
        return False

    def leave(self) -> None:
        """
        Put all non-blocking assignments here
        """
        for node, enabled in self._fsm_state_enabled_reg.items():
            self._fsm_state_enabled[node] = enabled
            if enabled:
                self._highlightNode(node)
            else:
                self._dehighlightNode(node)
        self._fsm_state_enabled_reg = {}

    def printStats(self) -> Dict[str, Any]:
        return {state: enabled for state, enabled in self._fsm_state_enabled.items()}

    def _modifyFSM(self) -> None:
        for loop in self._fsm.getLoops():
            self._loops.append(loop)

        # we need to extract the Loop portion from the FSM and add a state for the loop
        for i, loop in enumerate(self._loops):
            loopStart: pgv.Node = loop[1]
            loopEnd: pgv.Node = loop[0]

            # we need to add three states for each loop
            self._fsm.add_node(f"loop_{i}_entrance")
            self._fsm.add_node(f"loop_{i}_wait")
            self._fsm.add_node(f"loop_{i}_exit")

            entrance = self._fsm.get_node(f"loop_{i}_entrance")
            wait = self._fsm.get_node(f"loop_{i}_wait")
            loopexit = self._fsm.get_node(f"loop_{i}_exit")

            self._wait_states[wait] = loop

            # First, we connect loopStart's predecessor to loop_entrence
            toRemove: List[pgv.Edge] = []
            for pred in self._fsm.predecessors(loopStart):
                if pred != loopEnd:
                    self._fsm.add_edge(pred, entrance)
                toRemove.append((pred, loopStart))
            # Remove these edges
            for edge in toRemove:
                self._fsm.remove_edge(edge)

            # Second, we connect loopEnd's successor to loop_exit
            toRemove = []
            for succ in self._fsm.successors(loopEnd):
                self._fsm.add_edge(loopexit, succ)
                toRemove.append((loopEnd, succ))
            # Remove these edges
            for edge in toRemove:
                self._fsm.remove_edge(edge)

            self._fsm.add_edge(entrance, wait)
            self._fsm.add_edge(wait, wait)
            self._fsm.add_edge(wait, loopexit)

            # we need to add the loop
            self._loopEntrance[loop] = entrance
            self._loopWait[loop] = wait
            self._loopExit[loop] = loopexit
