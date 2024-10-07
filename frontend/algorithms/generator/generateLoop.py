from .generateFSM import *

from ..cfg import *


class LoopGenerator(FSMGenerator):
    def __init__(self, fsm: FSM) -> None:
        super().__init__(fsm)
        self._loopToStates: Dict[pgv.Edge, List[pgv.Node]] = {}

        self._stateEnabled: Dict[pgv.Node, BNode] = {}
        self._stateValid: Dict[pgv.Node, BNode] = {}
        self._stateStalled: Dict[pgv.Node, BNode] = {}

        # loop specific
        self._loopII: Dict[pgv.Edge, int] = {}
        self._loopBounds: Dict[pgv.Edge, int] = {}
        self._loopIIcounter: Dict[pgv.Edge, BNode] = {}
        self._loopStart: Dict[pgv.Edge, BNode] = {}
        self._loopIndVar: Dict[pgv.Edge, BNode] = {}

        self._loopIItoOffset: Dict[pgv.Edge, int] = {}

        # activation signals
        self._loop_activate_pipeline: Dict[pgv.Edge, BNode] = {}
        self._loop_begin_pipeline: Dict[pgv.Edge, BNode] = {}
        self._loop_active: Dict[pgv.Edge, BNode] = {}
        self._activate_loop: Dict[pgv.Edge, BNode] = {}

        # piepline exit
        self._loop_exit_cond: Dict[pgv.Edge, BNode] = {}
        self._loop_only_last_stage_enabled: Dict[pgv.Edge, BNode] = {}
        self._loop_epilogue: Dict[pgv.Edge, BNode] = {}
        self._loop_pipeline_finished: Dict[pgv.Edge, BNode] = {}

        # fsm stall
        self._fsm_stall: BNode = self.createWire("fsm_stall")

        # hyper things
        self._reset: BNode = self.createWire("reset")

        self._extractLoops()

    def run(self) -> None:
        # we create the parameter for each state
        super().run()

        # for loop in self._loops:
        #     self._generateHandShake(loop)
        self._generateStateTransition()

    def _generateHandShake(self, loop: pgv.Edge) -> None:
        states = self._loopToStates[loop]

        for i in range(len(states)):
            currState = states[i]
            # valid
            if not self._stateStalled[currState]:
                if i == 0:
                    self._stateValidReg[currState] = (
                        self._loopStart[loop]
                        and self._loopIIcounter[loop] == self._loopII[loop] - 1
                    )
                else:
                    self._stateValidReg[currState] = self._stateEnabled[states[i - 1]]
            if self._reset:
                self._stateValidReg[currState] = False

            # enabled
            self._stateEnabled[currState] = (
                self._stateValid[currState] and not self._stateStalled[currState]
            )

            # stalled
            if self._stateStalled[currState] and self._loopIIcounter[loop] != 0:
                self._stateStalled[currState] = True
            elif i + 1 < len(states):
                if self._stateStalled[states[i + 1]]:
                    self._stateStalled[currState] = True
            else:
                self._stateStalled[currState] = False

    def _generateStateTransition(self) -> None:
        allStates = self.getStates()
        allEdges = self.getEdges()

        # the state transition
        assignment = CaseAssignment(
            self._fsm_next_state, self._fsm_curr_state, event=combEventNode()
        )

        # add the state transition to enter the fsm using an input port start
        assert self._fsm.getIdleState() is not None, "FSM has no initial state"

        for edge in allEdges:
            start = edge[0]
            end = edge[1]
            currParamNode = self._fsm.getParamAtNode(start)

            if start == self._fsm.getIdleState():
                # add the idle state
                nextStateAssignment = self._getIdleStateAssignment()
            else:
                nextStateAssignment = self._getNextStateAssignment(end)
            assignment.addCase(currParamNode, nextStateAssignment)
        # add a default case to the current state
        assignment.addDefaultCase(
            WireAssignment(
                self._fsm_next_state, self._fsm_curr_state, isProcedural=True
            )
        )
        self.addAssignment(assignment)

    def _extractLoops(self) -> None:
        for i, loop in enumerate(self._fsm.getLoops()):
            loop_name = f"loop_{i}"
            # initialize the loop II
            self._loopII[loop] = int(self._fsm.getLoopII(loop))
            self._loopBounds[loop] = int(self._fsm.getLoopBound(loop))
            self._loopIIcounter[loop] = self.createReg(
                f"{loop_name}_IIcounter", width=math.ceil(math.log2(self._loopII[loop]))
            )
            self._loopStart[loop] = self.createReg(f"{loop_name}_start")
            self._loopIndVar[loop] = self.createReg(
                f"{loop_name}_indVar",
                width=math.ceil(math.log2(self._loopBounds[loop])),
            )

            self._loop_activate_pipeline[loop] = self.createReg(
                f"{loop_name}_activate_pipeline"
            )
            self._loop_begin_pipeline[loop] = self.createReg(
                f"{loop_name}_begin_pipeline"
            )
            self._loop_active[loop] = self.createReg(f"{loop_name}_active")
            self._activate_loop[loop] = self.createReg(f"{loop_name}_activate_loop")

            self._loop_exit_cond[loop] = self.createReg(f"{loop_name}_exit_cond")
            self._loop_only_last_stage_enabled[loop] = self.createReg(
                f"{loop_name}_only_last_stage_enabled"
            )
            self._loop_epilogue[loop] = self.createReg(f"{loop_name}_epilogue")
            self._loop_pipeline_finished[loop] = self.createReg(
                f"{loop_name}_pipeline_finished"
            )

            start = loop[1]
            finish = loop[0]

            # we traverse the states and find the loop
            states = []
            stack = [start]
            while stack:
                node = stack.pop()
                states.append(node)
                if node == finish:
                    break
                for succ in self._fsm.successors(node):
                    if succ in states:
                        # this should not happen
                        assert False, "Loop inside loop"
                    stack.append(succ)

            # TODO: we need to modify the state according to the scheduling
            self._loopIItoOffset[loop] = 0

            # add the loop
            self._loopToStates[loop] = states

            # we need to register the enable/valid/stall signals
            for state in states:
                self._stateEnabled[state] = self.createReg(f"{state}_enabled")
                self._stateValid[state] = self.createReg(f"{state}_valid")
                self._stateStalled[state] = self.createReg(f"{state}_stalled")
