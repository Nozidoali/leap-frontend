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
        self._loop_only_fast_stage_enabled: Dict[pgv.Edge, bool] = {}
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
            self._loop_only_fast_stage_enabled[loop] = False
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
            self._loopIItoState[loop] = states[0]

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

        # we highlight the states based on the stateEnabled
        for state, enabled in self._stateEnabled.items():
            if enabled:
                self._highlightNode(state)
            else:
                self._dehighlightNode(state)

    def _propagateLoopStates(self) -> None:
        for loop in self._loops:
            # execute the handshake
            self._executeHandshake(loop)

            self._checkLoopActivation(loop)

    def _executeHandshake(self, loop: pgv.Edge) -> None:
        states = self._loopToStates[loop]

        for i in range(len(states) - 1):
            currState = states[i]
            # valid
            if not self._stateStalled[currState]:
                if i == 0:
                    self._stateValidReg[currState] = (
                        self._loopStart[loop]
                        and self._loopIIcounter[loop] == self._loopII[loop]
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
        self._loop_exit_cond[loop] = self._loopIndVar[loop] == self._loopBounds[loop]

        if self._reset:
            self._loop_active_reg[loop] = False
        elif self._loop_activate_pipeline[loop]:
            self._loop_active_reg[loop] = True
        elif (
            not self._stateStalled[self._loopToStates[loop][0]]
            and self._loop_epilogue[loop]
            and self._loop_only_fast_stage_enabled[loop]
        ):
            self._loop_active_reg[loop] = False

        self._loop_begin_pipeline[loop] = False
        if self._reset:
            self._loop_begin_pipeline[loop] = False
        elif self._fsm_state_enabled[self._loopEntrance[loop]] and not self._fsm_stall:
            self._loop_begin_pipeline[loop] = True

    def _executeIIcounter(self, loop: pgv.Edge) -> None:
        self._loopIndVarReg[loop] = self._loopIndVar[loop]
        if self._reset:
            self._loopIndVarReg[loop] = 0
        elif self._activate_loop[loop]:
            self._loopIndVarReg[loop] = 0
        elif self._loopIIcounter[loop] == self._loopII[loop] - 1:
            state = self._loopIItoState[loop]
            if self._stateEnabled[state]:
                self._loopIndVarReg[loop] = self._loopIndVar[loop] + 1

    def _checkLoopEpilogue(self, loop: pgv.Edge) -> None:
        self._loop_epilogue[loop] = (
            self._loop_active[loop] and self._loop_exit_cond[loop]
        )
        if self._reset:
            self._loop_epilogue[loop] = False

        self._loop_epilogue_reg[loop] = self._loop_epilogue[loop]
        if self._reset:
            self._loop_epilogue_reg[loop] = False
        elif (
            self._stateEnabled[self._loopToStates[loop][0]]
            and self._loop_exit_cond[loop]
        ):
            self._loop_epilogue_reg[loop] = True
        elif (
            not self._stateStalled[self._loopToStates[loop][0]]
            and self._loop_epilogue[loop]
            and self._loop_only_fast_stage_enabled[loop]
        ):
            self._loop_epilogue_reg[loop] = False

        self._loop_pipeline_finished = (
            not self._stateStalled[self._loopToStates[loop][0]]
            and self._loop_epilogue[loop]
            and self._loop_only_fast_stage_enabled[loop]
        ) or self._loop_pipeline_finished[loop]

        self._loop_only_fast_stage_enabled[loop] = self._stateEnabled[
            self._loopToStates[loop][-1]
        ]
        for i in range(len(self._loopToStates[loop]) - 1):
            if not self._stateEnabled[self._loopToStates[loop][i]]:
                self._loop_only_fast_stage_enabled[loop] = False
                break

        self._loop_pipeline_finished_reg[loop] = self._loop_pipeline_finished[loop]
        if self._reset:
            self._loop_pipeline_finished_reg[loop] = False
        elif self._loop_activate_pipeline[loop]:
            self._loop_pipeline_finished_reg[loop] = False
