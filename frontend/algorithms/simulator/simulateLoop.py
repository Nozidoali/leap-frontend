from typing import List, Dict, Any
import pygraphviz as pgv

from ..cfg import *

from .simulateFSM import *


class LoopSimulator(FSMSimulator):

    def __init__(self, fsm: FSM) -> None:
        super().__init__(fsm)
        self._loopToStates: Dict[pgv.Edge, List[pgv.Node]] = {}

        # hand shakes
        self._stateEnabled: Dict[pgv.Node, bool] = {}
        self._stateValid: Dict[pgv.Node, bool] = {}
        self._stateStalled: Dict[pgv.Node, bool] = {}

        self._stateEnabledReg: Dict[pgv.Node, bool] = {}
        self._stateValidReg: Dict[pgv.Node, bool] = {}
        self._stateStalledReg: Dict[pgv.Node, bool] = {}

        self._loopII: Dict[pgv.Edge, int] = {}
        self._loopIIcounter: Dict[pgv.Edge, int] = {}
        self._loopBounds: Dict[pgv.Edge, int] = {}
        self._loopStart: Dict[pgv.Edge, bool] = {}
        self._loopIndVar: Dict[pgv.Edge, int] = {}

        self._loopIIcounterReg: Dict[pgv.Edge, int] = {}
        self._loopIItoState: Dict[pgv.Edge, pgv.Node] = {}
        self._loopIndVarReg: Dict[pgv.Edge, int] = {}

        # some boolean signals
        self._loop_activate_pipeline: Dict[pgv.Edge, bool] = {}
        self._loop_begin_pipeline: Dict[pgv.Edge, bool] = {}
        self._loop_active: Dict[pgv.Edge, bool] = {}
        self._activate_loop: Dict[pgv.Edge, bool] = {}

        self._loop_active_reg: Dict[pgv.Edge, bool] = {}

        # piepline exit
        self._loop_exit_cond: Dict[pgv.Edge, bool] = {}
        self._loop_only_last_stage_enabled: Dict[pgv.Edge, bool] = {}
        self._loop_epilogue: Dict[pgv.Edge, bool] = {}
        self._loop_pipeline_finished: Dict[pgv.Edge, bool] = {}

        self._loop_epilogue_reg: Dict[pgv.Edge, bool] = {}
        self._loop_pipeline_finished_reg: Dict[pgv.Edge, bool] = {}

        # fsm stall
        self._fsm_stall: bool = False

        # hyper things
        self._reset: bool = False

        # initialize the loop states
        self._extractLoops()

        self._fsm.write("fsm.dot")

    def _extractLoops(self) -> None:
        for loop in self._fsm.getLoops():
            # initialize the loop II
            self._loopII[loop] = int(self._fsm.getLoopII(loop))
            self._loopIIcounter[loop] = 0
            self._loopBounds[loop] = int(self._fsm.getLoopBound(loop))
            self._loopStart[loop] = False
            self._loopIndVar[loop] = 0

            self._loop_activate_pipeline[loop] = False
            self._loop_begin_pipeline[loop] = False
            self._loop_active[loop] = False
            self._activate_loop[loop] = False

            self._loop_exit_cond[loop] = False
            self._loop_only_last_stage_enabled[loop] = False
            self._loop_epilogue[loop] = False
            self._loop_pipeline_finished[loop] = False

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
            self._loopIItoState[loop] = states[1]

            # add the loop
            self._loopToStates[loop] = states

            # we need to register the enable/valid/stall signals
            for state in states:
                self._stateEnabled[state] = False
                self._stateValid[state] = False
                self._stateStalled[state] = False

        # for debugging
        # for loop, states in self._loopToStates.items():
        #     print(f"Loop: {loop}")
        #     print(f"States: {states}")

    def step(self) -> bool:
        done = super().step()
        if done:
            return True
        self._propagateLoopStates()

    def leave(self) -> None:
        super().leave()

        for state, enabled in self._stateEnabledReg.items():
            self._stateEnabled[state] = enabled
        self._stateEnabledReg = {}
        for state, valid in self._stateValidReg.items():
            self._stateValid[state] = valid
        self._stateValidReg = {}
        for state, stalled in self._stateStalledReg.items():
            self._stateStalled[state] = stalled
        self._stateStalledReg = {}

        for loop, indVar in self._loopIndVarReg.items():
            self._loopIndVar[loop] = indVar

        for loop, iiCounter in self._loopIIcounterReg.items():
            self._loopIIcounter[loop] = iiCounter

        for loop, active in self._loop_active_reg.items():
            self._loop_active[loop] = active

        for loop, epilogue in self._loop_epilogue_reg.items():
            self._loop_epilogue[loop] = epilogue
            
        for loop, pipelineFinished in self._loop_pipeline_finished_reg.items():
            self._loop_pipeline_finished[loop] = pipelineFinished

        # we highlight the states based on the stateEnabled
        for state, enabled in self._stateEnabled.items():
            if enabled:
                self._highlightNode(state)
            else:
                self._dehighlightNode(state)

    def printStats(self) -> Dict[str, Any]:
        stats = super().printStats()

        print(f"\n{'States':<10} | {'Enabled':<8} | {'Valid':<6} | {'Stalled':<8}")
        for state in self._stateEnabled:
            isEnable = self._stateEnabled[state]
            isValid = self._stateValid[state]
            isStalled = self._stateStalled[state]

            # format print
            print(
                f"{str(state):<10} | {str(isEnable):<8} | {str(isValid):<6} | {str(isStalled):<8}"
            )
        print(
            f"\n{'Loop':<20} | {'Active':<8} | {'Pipeline':<8} | {'Epilogue':<8} | {'Finished':<8} | {'Start':<8} | {'Activating':<10} | {'Exit Cond':<10} | {'Last Stage':<10}"
        )
        for loop in self._loops:
            isActive = self._loop_active[loop]
            isPipeline = self._loop_activate_pipeline[loop]
            isEpilogue = self._loop_epilogue[loop]
            isFinished = self._loop_pipeline_finished[loop]
            isStart = self._loopStart[loop]
            isActivating = self._activate_loop[loop]
            isExitCond = self._loop_exit_cond[loop]
            isLastStage = self._loop_only_last_stage_enabled[loop]

            print(
            f"{str(loop):<20} | {str(isActive):<8} | {str(isPipeline):<8} | {str(isEpilogue):<8} | {str(isFinished):<8} | {str(isStart):<8} | {str(isActivating):<10} | {str(isExitCond):<10} | {str(isLastStage):<10}"
            )

        print(f"\n{'Loop':<20} | {'II':<8} | {'II Cnt':<6} | {'IndVar':<8} | {'Bounds':<8}")
        for loop in self._loopII:
            loop_ii = self._loopII[loop]
            loop_ii_counter = self._loopIIcounter[loop]
            loop_ind_var = self._loopIndVar[loop]
            loop_bounds = self._loopBounds[loop]

            print(
            f"{str(loop):<20} | {str(loop_ii):<8} | {str(loop_ii_counter):<6} | {str(loop_ind_var):<8} | {str(loop_bounds):<8}"
            )


    def _propagateLoopStates(self) -> None:
        for loop in self._loops:
            # execute the handshake
            self._executeHandshake(loop)
            self._checkLoopActivation(loop)
            self._executeIIcounter(loop)
            self._checkLoopEpilogue(loop)

    def _executeHandshake(self, loop: pgv.Edge) -> None:
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

    def _checkLoopActivation(self, loop: pgv.Edge) -> bool:
        # Step 1
        # loop begin pipeline
        self._loop_begin_pipeline[loop] = False
        if self._reset:
            self._loop_begin_pipeline[loop] = False
        elif self._fsm_state_enabled[self._loopEntrance[loop]] and not self._fsm_stall:
            self._loop_begin_pipeline[loop] = True

        self._loop_activate_pipeline[loop] = (
            not self._fsm_stall and self._loop_begin_pipeline[loop]
        ) and not self._loop_active[loop]

        self._loopStart[loop] = self._loop_activate_pipeline[loop] or (
            (self._loop_active[loop] and not self._loop_epilogue[loop])
            and not (
                (
                    self._stateEnabled[self._loopToStates[loop][0]]
                    and self._loop_exit_cond[loop]
                )
            )
        )
        if self._reset:
            self._loopStart[loop] = False

        self._activate_loop[loop] = (
            not self._fsm_stall and self._loop_begin_pipeline[loop]
        ) and not self._loop_active[loop]

        # TODO: double check the boundar
        # because most of the case we need to minus 2
        self._loop_exit_cond[loop] = self._loopIndVar[loop] == self._loopBounds[loop] - 2

        if self._reset:
            self._loop_active_reg[loop] = False
        if self._loop_activate_pipeline[loop]:
            self._loop_active_reg[loop] = True
        if (
            not self._stateStalled[self._loopToStates[loop][0]]
            and self._loop_epilogue[loop]
            and self._loop_only_last_stage_enabled[loop]
        ):
            self._loop_active_reg[loop] = False

    def _executeIIcounter(self, loop: pgv.Edge) -> None:
        if self._reset:
            self._loopIndVarReg[loop] = 0
        elif self._activate_loop[loop]:
            self._loopIndVarReg[loop] = 0
        state = self._loopIItoState[loop]
        if self._stateEnabled[state] and self._loopIIcounter[loop] == 1:
            self._loopIndVarReg[loop] = self._loopIndVar[loop] + 1

        self._loopIIcounterReg[loop] = self._loopIIcounter[loop] + 1
        if self._reset:
            self._loopIIcounterReg[loop] = 0
        elif self._loopIIcounter[loop] == self._loopII[loop] - 1:
            self._loopIIcounterReg[loop] = 0

    def _checkLoopEpilogue(self, loop: pgv.Edge) -> None:

        if self._reset:
            self._loop_epilogue_reg[loop] = False
        else:
            if (
                self._stateEnabled[self._loopToStates[loop][0]]
                and self._loop_exit_cond[loop]
            ):
                self._loop_epilogue_reg[loop] = True
            elif (
                not self._stateStalled[self._loopToStates[loop][0]]
                and self._loop_epilogue[loop]
                and self._loop_only_last_stage_enabled[loop]
            ):
                self._loop_epilogue_reg[loop] = False

        self._loop_pipeline_finished[loop] = (
            not self._stateStalled[self._loopToStates[loop][0]]
            and self._loop_epilogue[loop]
            and self._loop_only_last_stage_enabled[loop]
        ) or self._loop_pipeline_finished[loop]

        self._loop_only_last_stage_enabled[loop] = self._stateEnabled[
            self._loopToStates[loop][-1]
        ]
        for i in range(len(self._loopToStates[loop]) - 1):
            if not self._stateEnabled[self._loopToStates[loop][i]]:
                self._loop_only_last_stage_enabled[loop] = False
                break

        self._loop_pipeline_finished_reg[loop] = self._loop_pipeline_finished[loop]
        if self._reset:
            self._loop_pipeline_finished_reg[loop] = False
        elif self._loop_activate_pipeline[loop]:
            self._loop_pipeline_finished_reg[loop] = False
