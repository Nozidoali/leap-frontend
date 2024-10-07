from .generateFSM import *

from ..cfg import *


class LoopGenerator(FSMGenerator):
    def __init__(self, fsm: FSM) -> None:
        super().__init__(fsm)
        self._loopToStates: Dict[pgv.Edge, List[pgv.Node]] = {}

        self._stateEnabled: Dict[pgv.Node, BNode] = {}
        self._stateValid: Dict[pgv.Node, BNode] = {}
        self._stateStalled: Dict[pgv.Node, BNode] = {}

        self._stateStalledReg: Dict[pgv.Node, BNode] = {}

        # loop specific
        self._loopII: Dict[pgv.Edge, int] = {}
        self._loopBounds: Dict[pgv.Edge, int] = {}
        self._loopIIcounter: Dict[pgv.Edge, BNode] = {}
        self._loopStart: Dict[pgv.Edge, BNode] = {}
        self._loopIndVar: Dict[pgv.Edge, BNode] = {}
        self._loopIIcounterBound: Dict[pgv.Edge, BNode] = {}

        self._loopIItoOffset: Dict[pgv.Edge, int] = {}

        # activation signals
        self._loop_activate_pipeline: Dict[pgv.Edge, BNode] = {}
        self._loop_begin_pipeline: Dict[pgv.Edge, BNode] = {}
        self._loop_active: Dict[pgv.Edge, BNode] = {}

        # piepline exit
        self._loop_exit_cond: Dict[pgv.Edge, BNode] = {}
        self._loop_only_last_stage_enabled: Dict[pgv.Edge, BNode] = {}
        self._loop_epilogue: Dict[pgv.Edge, BNode] = {}
        self._loop_pipeline_finished: Dict[pgv.Edge, BNode] = {}

        self._loop_pipeline_finished_reg: Dict[pgv.Edge, BNode] = {}

        self._extractLoops()

    def run(self) -> None:
        # we create the parameter for each state
        super().run()
        self._generateOutputs()

        for loop in self._loops:
            self._generateHandShake(loop)
            self._generateLoopActivation(loop)
            self._genreateLoopDeactivation(loop)
            self._generateLoopIICounter(loop)
        self._generateStateTransition()

    def _generateOutputs(self) -> None:
        for node in self._fsm.nodes():
            if (
                self.isWaitState(node)
                or self.isEntranceState(node)
                or self.isExitState(node)
            ):
                continue
            self._generateStateOutput(node)

    def _generateStateOutput(self, node: pgv.Node) -> None:
        if node in self._regular_nodes:
            outName = f"{node.name}_ctrl_out"
            outNode = VarNode(outName)
            self.module.addPort(OutputPort(outNode, BasicRange(1)))
            paramNode = self._fsm.getParamAtNode(node)
            compNode = eqNode(self._fsm_curr_state, paramNode)
            self.addAssignment(WireAssignment(outNode, compNode))
            return
        else:
            assert (
                node in self._stateEnabled
            ), f"Node {node} is not in {self._stateEnabled}"
            outName = f"{node.name}_ctrl_out"
            outNode = VarNode(outName)
            self.module.addPort(OutputPort(outNode, BasicRange(1)))
            enableNode = self._stateEnabled[node]
            self.addAssignment(WireAssignment(outNode, enableNode))
            return

    def _generateLoopIICounter(self, loop: pgv.Edge) -> None:
        # step 1
        # loop indvar
        assignmentIndVar = ConditionalAssignment(
            self._loopIndVar[loop], event=seqEventNode()
        )
        assignmentIndVar.addBranch(
            self._reset,
            RegAssignment(self._loopIndVar[loop], ConstantNode("1'b0")),
        )
        assignmentIndVar.addBranch(
            self._loop_activate_pipeline[loop],
            RegAssignment(self._loopIndVar[loop], ConstantNode("1'b0")),
        )
        offset = self._loopIItoOffset[loop]
        state = self._loopToStates[loop][offset]
        assignmentIndVar.addBranch(
            andNode(
                self.nodeIIisBound(loop),
                self._stateEnabled[state],
            ),
            RegAssignment(
                self._loopIndVar[loop],
                plusNode(self._loopIndVar[loop], ConstantNode("1")),
            ),
        )
        self.addAssignment(assignmentIndVar)

        # step 2
        # loop II counter
        IIwidth = math.ceil(math.log2(self._loopII[loop]))
        constNode = ConstantNode(f"{IIwidth}'d0")
        increNode = ConstantNode(f"{IIwidth}'d1")
        assignmentIIcounter = ConditionalAssignment(
            self._loopIIcounter[loop], event=seqEventNode()
        )
        assignmentIIcounter.addBranch(
            self._reset,
            RegAssignment(self._loopIIcounter[loop], constNode),
        )
        assignmentIIcounter.addBranch(
            self.nodeIIisBound(loop),
            RegAssignment(self._loopIIcounter[loop], constNode),
        )
        assignmentIIcounter.addDefaultBranch(
            RegAssignment(
                self._loopIIcounter[loop],
                plusNode(self._loopIIcounter[loop], increNode),
            ),
        )
        self.addAssignment(assignmentIIcounter)

    def _generateHandShake(self, loop: pgv.Edge) -> None:
        states = self._loopToStates[loop]

        for i in range(len(states)):
            currState = states[i]

            # valid
            assignmentValid = ConditionalAssignment(
                self._stateValid[currState], event=combEventNode()
            )
            # the reset condition should be the first state
            assignmentValid.addBranch(
                self._reset,
                RegAssignment(self._stateValid[currState], ConstantNode("1'b0")),
            )
            if i == 0:
                assignmentValid.addBranch(
                    notNode(self._stateStalled[currState]),
                    RegAssignment(
                        self._stateValid[currState],
                        andNode(self.nodeIIisBound(loop), self._loopStart[loop]),
                    ),
                )
            else:
                assignmentValid.addBranch(
                    notNode(self._stateStalled[currState]),
                    RegAssignment(
                        self._stateValid[currState], self._stateEnabled[states[i - 1]]
                    ),
                )
            self.addAssignment(assignmentValid)

            # enabled
            assignmentEnabled = WireAssignment(
                self._stateEnabled[currState],
                andNode(
                    self._stateValid[currState], notNode(self._stateStalled[currState])
                ),
            )
            self.addAssignment(assignmentEnabled)

            # stalled

            assignmentStalled = ConditionalAssignment(
                self._stateStalled[currState], event=seqEventNode()
            )
            assignmentStalled.addBranch(
                andNode(self._stateStalledReg[currState], self.nodeIIisNotBound(loop)),
                LatchAssignment(self._stateStalled[currState], ConstantNode("1'b1")),
            )
            if i + 1 < len(states):
                nextState = states[i + 1]
                assignmentStalled.addBranch(
                    self._stateStalled[nextState],
                    LatchAssignment(
                        self._stateStalled[currState], ConstantNode("1'b1")
                    ),
                )
            assignmentStalled.addDefaultBranch(
                LatchAssignment(self._stateStalled[currState], ConstantNode("1'b0")),
            )
            self.addAssignment(assignmentStalled)

    def _generateLoopActivation(self, loop: pgv.Edge) -> None:
        # loop begin pipeline
        assignmentBegin = ConditionalAssignment(
            self._loop_begin_pipeline[loop], event=combEventNode()
        )
        assignmentBegin.addBranch(
            self._reset,
            LatchAssignment(self._loop_begin_pipeline[loop], ConstantNode("1'b0")),
        )
        assignmentBegin.addBranch(
            andNode(self.currStateIsEntrance(loop), self.nodeNotStall()),
            LatchAssignment(self._loop_begin_pipeline[loop], ConstantNode("1'b1")),
        )
        assignmentBegin.addDefaultBranch(
            LatchAssignment(self._loop_begin_pipeline[loop], ConstantNode("1'b0")),
        )
        self.addAssignment(assignmentBegin)

        # step 2:
        # loop activate pipeline
        assignmentActivatePipeline = LatchAssignment(
            self._loop_activate_pipeline[loop],
            andNode(
                andNode(self.nodeNotStall(), self._loop_begin_pipeline[loop]),
                notNode(self._loop_active[loop]),
            ),
            event=combEventNode(),
        )
        self.addAssignment(assignmentActivatePipeline)

        # step 3:
        # loop start
        assignmentStart = ConditionalAssignment(
            self._loopStart[loop], event=combEventNode()
        )
        assignmentStart.addBranch(
            self._reset,
            LatchAssignment(self._loopStart[loop], ConstantNode("1'b0")),
        )
        assignmentStart.addDefaultBranch(
            LatchAssignment(self._loopStart[loop], self.loopStartCondition(loop)),
        )
        self.addAssignment(assignmentStart)

        # step 4:
        # loop active
        assignmentLoopActive = ConditionalAssignment(
            self._loop_active[loop], event=seqEventNode()
        )
        assignmentLoopActive.addBranch(
            self._reset,
            RegAssignment(self._loop_active[loop], ConstantNode("1'b0")),
        )
        assignmentLoopActive.addBranch(
            self._loop_activate_pipeline[loop],
            RegAssignment(self._loop_active[loop], ConstantNode("1'b1")),
        )
        assignmentLoopActive.addBranch(
            self.loopNotActiveCondition(loop),
            RegAssignment(self._loop_active[loop], ConstantNode("1'b0")),
        )
        self.addAssignment(assignmentLoopActive)

    def _genreateLoopDeactivation(self, loop: pgv.Edge) -> None:
        # step 1:
        # loop exit condition
        assignmentExit = LatchAssignment(
            self._loop_exit_cond[loop],
            self.loopExitCondition(loop),
            event=combEventNode(),
        )
        self.addAssignment(assignmentExit)

        # step 2:
        # loop only last stage enabled
        assignmentOnlyLastStageEnabled = LatchAssignment(
            self._loop_only_last_stage_enabled[loop],
            self.onlyLastStageEnabledCondition(loop),
            event=combEventNode(),
        )
        self.addAssignment(assignmentOnlyLastStageEnabled)

        # step 3:
        # loop epilogue
        assignmentEpilogue = ConditionalAssignment(
            self._loop_epilogue[loop], event=seqEventNode()
        )
        assignmentEpilogue.addBranch(
            self._reset,
            RegAssignment(self._loop_epilogue[loop], ConstantNode("1'b0")),
        )
        assignmentEpilogue.addBranch(
            andNode(
                self._stateEnabled[self._loopToStates[loop][0]],
                self._loop_exit_cond[loop],
            ),
            RegAssignment(self._loop_epilogue[loop], ConstantNode("1'b1")),
        )
        assignmentEpilogue.addBranch(
            self.loopNotActiveCondition(loop),
            RegAssignment(self._loop_epilogue[loop], ConstantNode("1'b0")),
        )
        self.addAssignment(assignmentEpilogue)

        # step 4:
        # loop pipeline finished
        assignmentPipelineFinished = LatchAssignment(
            self._loop_pipeline_finished[loop],
            orNode(
                self.loopNotActiveCondition(loop),
                self._loop_pipeline_finished_reg[loop],
            ),
            event=combEventNode(),
        )
        self.addAssignment(assignmentPipelineFinished)

        # step 5:
        # loop pipeline finished reg
        assignmentPipelineFinishedReg = ConditionalAssignment(
            self._loop_pipeline_finished_reg[loop], event=seqEventNode()
        )
        assignmentPipelineFinishedReg.addBranch(
            self._reset,
            RegAssignment(self._loop_pipeline_finished_reg[loop], ConstantNode("1'b0")),
        )
        assignmentPipelineFinishedReg.addBranch(
            self._loop_activate_pipeline[loop],
            RegAssignment(self._loop_pipeline_finished_reg[loop], ConstantNode("1'b0")),
        )
        assignmentPipelineFinishedReg.addDefaultBranch(
            RegAssignment(
                self._loop_pipeline_finished_reg[loop],
                self._loop_pipeline_finished[loop],
            ),
        )
        self.addAssignment(assignmentPipelineFinishedReg)

    def _generateStateTransition(self) -> None:
        allStates = self.getStates()
        allEdges = self.getEdges()

        # the state transition
        assignment = CaseAssignment(
            self._fsm_next_state, self._fsm_curr_state, event=seqEventNode()
        )

        # add the state transition to enter the fsm using an input port start
        assert self._fsm.getIdleState() is not None, "FSM has no initial state"

        for start in allStates:
            if self.isWaitState(start):
                continue

            currParamNode = self._fsm.getParamAtNode(start)

            if start == self._fsm.getIdleState():
                # add the idle state
                nextStateAssignment = self._getIdleStateAssignment()
            else:
                successors = []
                for edge in allEdges:
                    if edge[0] == start:
                        successors.append(edge[1])
                if len(successors) == 0:
                    continue
                if len(successors) == 1:
                    nextParamNode = self._fsm.getParamAtNode(successors[0])
                    nextStateAssignment = FSMGenerator._stateTransitionAssignment(
                        self.nextStateNode, nextParamNode
                    )
                else:
                    print(f"State {start} has multiple successors = {successors}")
                    nextStateAssignment = ConditionalAssignment(self._fsm_next_state)
                    for j, succ in enumerate(successors[:-1]):
                        controlNode = self._fsm.getControlSignalAtNode(succ, j)

                        # we need to create an input port for the control signal
                        self.module.addPort(InputPort(controlNode, BasicRange(1)))

                        nextParamNode = self._fsm.getParamAtNode(succ)
                        nextStateAssignment.addBranch(
                            controlNode,
                            FSMGenerator._stateTransitionAssignment(
                                self.nextStateNode, nextParamNode
                            ),
                        )
                    # add a default case to the conditional assignment
                    nextParamNode = self._fsm.getParamAtNode(successors[-1])
                    nextStateAssignment.addDefaultBranch(
                        FSMGenerator._stateTransitionAssignment(
                            self.nextStateNode, nextParamNode
                        ),
                    )
            assignment.addCase(currParamNode, nextStateAssignment)

        for loop in self._loops:
            # add the transition from the wait
            waitState: pgv.Node = self.getWaitState(loop)
            exitState: pgv.Node = self.getExitState(loop)
            paramNode: BNode = self._fsm.getParamAtNode(waitState)
            nextParamNode: BNode = self._fsm.getParamAtNode(exitState)
            nextStateAssignment: BNEdge = ConditionalAssignment(self._fsm_next_state)
            nextStateAssignment.addBranch(
                andNode(self._loop_pipeline_finished[loop], self.nodeNotStall()),
                FSMGenerator._stateTransitionAssignment(
                    self._fsm_next_state, nextParamNode
                ),
            )

            assignment.addCase(paramNode, nextStateAssignment)

        # add a default case to the current state
        assignment.addDefaultCase(
            WireAssignment(
                self._fsm_next_state, self._fsm_curr_state, isProcedural=True
            )
        )
        self.addAssignment(assignment)

    def nodeIIisBound(self, loop: pgv.Edge) -> BNode:
        return eqNode(self._loopIIcounter[loop], self._loopIIcounterBound[loop])

    def nodeIIisNotBound(self, loop: pgv.Edge) -> BNode:
        return neqNode(self._loopIIcounter[loop], self._loopIIcounterBound[loop])

    def currStateIsEntrance(self, loop: pgv.Edge) -> BNode:
        return eqNode(self._fsm_curr_state, self.getEntranceParam(loop))

    def loopStartCondition(self, loop: pgv.Edge) -> BNode:
        return andNode(
            orNode(
                self._loop_activate_pipeline[loop],
                andNode(self._loop_active[loop], notNode(self._loop_epilogue[loop])),
            ),
            notNode(
                andNode(
                    self._stateEnabled[self._loopToStates[loop][0]],
                    self._loop_exit_cond[loop],
                )
            ),
        )

    def onlyLastStageEnabledCondition(self, loop: pgv.Edge) -> BNode:
        lastState = self._loopToStates[loop][-1]
        retNode = self._stateEnabled[lastState]
        for state in self._loopToStates[loop][:-1]:
            retNode = andNode(notNode(self._stateEnabled[state]), retNode)
        return retNode

    def loopNotActiveCondition(self, loop: pgv.Edge) -> BNode:
        return andNode(
            andNode(
                notNode(self._stateStalled[self._loopToStates[loop][0]]),
                self._loop_epilogue[loop],
            ),
            self._loop_only_last_stage_enabled[loop],
        )

    def loopExitCondition(self, loop: pgv.Edge) -> BNode:
        loopBoundWidth = math.ceil(math.log2(self._loopBounds[loop]))
        loopBoundNode = ConstantNode(f"{loopBoundWidth}'d{self._loopBounds[loop]-1}")
        return eqNode(self._loopIndVar[loop], loopBoundNode)

    def _extractLoops(self) -> None:
        for i, loop in enumerate(self._fsm.getLoops()):
            loop_name = f"loop_{i}"
            # initialize the loop II
            self._loopII[loop] = int(self._fsm.getLoopII(loop))
            self._loopBounds[loop] = int(self._fsm.getLoopBound(loop))
            self._loopIIcounter[loop] = self.createReg(
                f"{loop_name}_IIcounter", width=math.ceil(math.log2(self._loopII[loop]))
            )
            ii_counter_bound = self._loopII[loop] - 1
            ii_counter_width = math.ceil(math.log2(self._loopII[loop]))

            self._loopIIcounterBound[loop] = ConstantNode(
                f"{ii_counter_width}'d{ii_counter_bound}"
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

            self._loop_exit_cond[loop] = self.createReg(f"{loop_name}_exit_cond")
            self._loop_only_last_stage_enabled[loop] = self.createReg(
                f"{loop_name}_only_last_stage_enabled"
            )
            self._loop_epilogue[loop] = self.createReg(f"{loop_name}_epilogue")
            self._loop_pipeline_finished[loop] = self.createReg(
                f"{loop_name}_pipeline_finished"
            )

            self._loop_pipeline_finished_reg[loop] = self.createReg(
                f"{loop_name}_pipeline_finished_reg"
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

                self._stateStalledReg[state] = self.createWire(f"{state}_stalled_reg")
