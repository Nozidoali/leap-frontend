from typing import List, Dict
import math

from ..cfg import *
from ...modules import *
from .generateModule import *


class FSMGenerator(ModuleGenerator):
    def __init__(self, fsm: FSM) -> None:
        # This will initialize a module
        super().__init__()

        # fsm state enabled
        self._fsm: FSM = fsm

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

        # fsm stall
        self._fsm_stall: BNode = self.createWire("fsm_stall")

        self._modifyFSM()
        self._bindFSM()

        # self._fsm.write("tmp.dot")

    def run(self) -> None:
        self._generateInferface()
        # we create the parameter for each state
        self._generateState()
        self._fsmExitGeneration()
        self._fsmCurrentStateAssignment()
        pass

    def _bindFSM(self) -> None:
        self._catagorizeEdges()

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

    def isWaitState(self, node: pgv.Node) -> bool:
        return node in self._wait_states

    def isEntranceState(self, node: pgv.Node) -> bool:
        return node in self._loopEntrance.values()

    def isExitState(self, node: pgv.Node) -> bool:
        return node in self._loopExit.values()

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
                currEdge = self._fsm.get_edge(node, succ)
                if currEdge in self._regular_edges:
                    continue
                self._regular_edges.append(self._fsm.get_edge(node, succ))

        # for debugging
        # for edge in self._regular_edges:
        #     print(edge)

    def getStates(self) -> List[pgv.Node]:
        return self._regular_nodes

    def getEdges(self) -> List[pgv.Edge]:
        return self._regular_edges

    def getLoops(self) -> List[pgv.Edge]:
        return self._loops

    def _generateState(self):
        assert len(self.getStates()) > 0, "FSM is empty"
        width: int = math.ceil(math.log2(len(self.getStates())))

        nextStateNode = VarNode("next_state")
        currStateNode = VarNode("curr_state")
        self.module.addPort(RegPort(nextStateNode, BasicRange(width)))
        self.module.addPort(RegPort(currStateNode, BasicRange(width)))
        for i, node in enumerate(self.getStates()):
            # we define each state as a parameter
            paramNode = self._fsm.getParamAtNode(node)
            self.module.addPort(ParameterPort(paramNode, BasicRange(width)))
            self.module.addAssignment(
                Assignment(paramNode, ConstantNode(f"{width}'d{i}"))
            )

        self._fsm_next_state: BNode = nextStateNode
        self._fsm_curr_state: BNode = currStateNode

    @property
    def nextStateNode(self) -> BNode:
        return self._fsm_next_state

    @property
    def currStateNode(self) -> BNode:
        return self._fsm_curr_state

    def _getIdleStateAssignment(self) -> BNEdge:
        idleState = self._fsm.getIdleState()
        assert (
            len(self._fsm.successors(idleState)) == 1
        ), "Idle state has more than one successors"
        succ = self._fsm.successors(idleState)[0]
        nextParamNode = self._fsm.getParamAtNode(succ)
        nextStateAssignment = ConditionalAssignment(self.nextStateNode)
        startNode = VarNode("start")
        nextStateAssignment.addBranch(
            startNode,
            FSMGenerator._stateTransitionAssignment(self.nextStateNode, nextParamNode),
        )
        nextStateAssignment.addDefaultBranch(
            FSMGenerator._stateTransitionAssignment(
                self.nextStateNode, self.currStateNode
            )
        )
        return nextStateAssignment

    @staticmethod
    def _stateTransitionAssignment(nextStateNode: VarNode, succNode: VarNode) -> BNEdge:
        return LatchAssignment(nextStateNode, succNode)

    def _generateInferface(self):
        # for each bb with more than one successor, we need an input port
        # for bb in fsm.bbs:
        #     for i in range(fsm.numSuccessors(bb) - 1):
        #         inputNode = fsm.getControlSignalAtBB(bb, i)
        #         module.addPort(InputPort(inputNode, BasicRange(1)))

        # for node in fsm.nodes():
        #     # for each parameter, we need to output a control signal, which is the comparison between the current state and the parameter
        #     paramNode = fsm.getParamAtNode(node)
        #     compNode = OPNode("==", OPType.BINARY_EQ, currStateNode, paramNode)
        #     outName = node.name + "_ctrl_out"
        #     outNode = VarNode(outName)
        #     module.addPort(OutputPort(outNode, BasicRange(1)))
        #     module.addAssignment(Assignment(outNode, compNode))

        # generate the clk and reset ports
        clkNode = VarNode("clk")
        resetNode = VarNode("reset")
        self.module.addPort(InputPort(clkNode, BasicRange(1)))
        self.module.addPort(InputPort(resetNode, BasicRange(1)))

        self._clk = clkNode
        self._reset = resetNode

        # generate the start and finish ports
        startNode = VarNode("start")
        finishNode = VarNode("finish")
        self.module.addPort(InputPort(startNode, BasicRange(1)))
        self.module.addPort(OutputRegPort(finishNode, BasicRange(1)))

        self._start = startNode
        self._finish = finishNode

    def _fsmExitGeneration(self):
        finishNode = VarNode("finish")
        finalStateParam = self._fsm.getParamAtNode(self._fsm.getFinalState())
        finishAssignment = ConditionalAssignment(finishNode, event=seqEventNode())
        finishAssignment.addBranch(
            OPNode("==", OPType.BINARY_EQ, self.currStateNode, finalStateParam),
            RegAssignment(finishNode, ConstantNode("1'b1")),
        )
        finishAssignment.addDefaultBranch(
            RegAssignment(finishNode, ConstantNode("1'b0"))
        )
        self.module.addAssignment(finishAssignment)

    def _fsmCurrentStateAssignment(self) -> None:
        """
        CurrState is a register that is updated with the next state
        when reset is high, the current state is set to the idle state
        """
        resetNode = VarNode("reset")
        idleStateNode = VarNode(self._fsm.getIdleState().name + "_label")

        assignment = ConditionalAssignment(
            self.currStateNode, event=seqEventNode(useReset=True)
        )
        assignment.addBranch(
            resetNode, RegAssignment(self.currStateNode, idleStateNode)
        )
        assignment.addDefaultBranch(
            RegAssignment(self.currStateNode, self.nextStateNode)
        )
        self.module.addAssignment(assignment)

    def getEntranceParam(self, loop: pgv.Edge) -> BNode:
        return self._fsm.getParamAtNode(self._loopEntrance[loop])

    def nodeNotStall(self) -> BNode:
        return notNode(self._fsm_stall)
