import math
from .graph import *
from .fsm import *
from ...modules import *


def _fsmStateGeneration(fsm: FSM, module: Module):
    assert len(fsm.nodes()) > 0, "FSM is empty"
    width: int = math.ceil(math.log2(len(fsm.nodes())))

    nextStateNode = VarNode("next_state")
    currStateNode = VarNode("curr_state")
    module.addPort(WirePort(nextStateNode, BasicRange(width)))
    module.addPort(RegPort(currStateNode, BasicRange(width)))
    for i, node in enumerate(fsm.nodes()):
        # we define each state as a parameter
        paramNode = fsm.getParamAtNode(node)
        module.addPort(ParameterPort(paramNode, BasicRange(width)))
        module.addAssignment(Assignment(paramNode, ConstantNode(f"3'd{i}")))
    return nextStateNode, currStateNode


def _getNextStateAssignment(fsm: FSM, node: VarNode, nextStateNode: VarNode) -> BNEdge:
    assert len(fsm.successors(node)) >= 1, "Node has no successors"

    if len(fsm.successors(node)) == 1:
        succ = fsm.successors(node)[0]
        nextParamNode = fsm.getParamAtNode(succ)
        return WireAssignment(nextStateNode, nextParamNode, isProcedural=True)
    else:
        conditionalAssignment = ConditionalAssignment(nextStateNode)
        for j, succ in enumerate(fsm.successors(node)[:-1]):
            controlNode = fsm.getControlSignalAtNode(succ, j)
            nextParamNode = fsm.getParamAtNode(succ)
            conditionalAssignment.addBranch(
                controlNode,
                WireAssignment(
                    nextStateNode,
                    nextParamNode,
                    isProcedural=True,
                ),
            )
        # add a default case to the conditional assignment
        nextParamNode = fsm.getParamAtNode(fsm.successors(node)[-1])
        conditionalAssignment.addDefaultBranch(
            WireAssignment(nextStateNode, nextParamNode, isProcedural=True)
        )
        return conditionalAssignment


def _fsmCurrentStateAssignment(
    fsm: FSM, module: Module, nextStateNode: VarNode, currStateNode: VarNode
) -> BNEdge:
    """
    CurrState is a register that is updated with the next state
    when reset is high, the current state is set to the idle state
    """
    resetNode = VarNode("reset")
    idleStateNode = VarNode(fsm.getIdleState().name + "_label")

    assignment = ConditionalAssignment(currStateNode, event=seqEventNode(useReset=True))
    assignment.addBranch(resetNode, RegAssignment(currStateNode, idleStateNode))
    assignment.addDefaultBranch(RegAssignment(currStateNode, nextStateNode))
    module.addAssignment(assignment)


def _getIdleStateAssignment(
    fsm: FSM, nextStateNode: VarNode, currStateNode: VarNode
) -> BNEdge:
    idleState = fsm.getIdleState()
    assert (
        len(fsm.successors(idleState)) == 1
    ), "Idle state has more than one successors"
    succ = fsm.successors(idleState)[0]
    nextParamNode = fsm.getParamAtNode(succ)
    nextStateAssignment = ConditionalAssignment(nextStateNode)
    startNode = VarNode("start")
    nextStateAssignment.addBranch(
        startNode, WireAssignment(nextStateNode, nextParamNode, isProcedural=True)
    )
    nextStateAssignment.addDefaultBranch(
        WireAssignment(nextStateNode, currStateNode, isProcedural=True)
    )
    return nextStateAssignment


def _fsmStateTransitionGeneration(
    fsm: FSM, module: Module, nextStateNode: VarNode, currStateNode: VarNode
):
    """
    This function generates the state transition logic for the FSM
    It is implemented using a case statement in the module

    the target is the next state, and the source is the current state
    """
    # for each state transition, we need to update the next state

    # NOTE: it must be in a always block
    assignment = CaseAssignment(nextStateNode, currStateNode, event=combEventNode())

    # add the state transition to enter the fsm using an input port start
    assert fsm.getIdleState() is not None, "FSM has no initial state"

    for node in fsm.nodes():
        currParamNode = fsm.getParamAtNode(node)
        if len(fsm.successors(node)) == 0:
            continue
        if node == fsm.getIdleState():
            # add the idle state
            nextStateAssignment = _getIdleStateAssignment(
                fsm, nextStateNode, currStateNode
            )
        else:
            nextStateAssignment = _getNextStateAssignment(fsm, node, nextStateNode)
        assignment.addCase(currParamNode, nextStateAssignment)
    # add a default case to the current state
    assignment.addDefaultCase(
        WireAssignment(nextStateNode, currStateNode, isProcedural=True)
    )
    # add the case assignment to the module
    module.addAssignment(assignment)


def _fsmInterfaceGeneration(
    fsm: FSM, module: Module, nextStateNode: VarNode, currStateNode: VarNode
):
    # for each bb with more than one successor, we need an input port
    for bb in fsm.bbs:
        for i in range(fsm.numSuccessors(bb) - 1):
            inputNode = fsm.getControlSignalAtBB(bb, i)
            module.addPort(InputPort(inputNode, BasicRange(1)))

    for node in fsm.nodes():
        # for each parameter, we need to output a control signal, which is the comparison between the current state and the parameter
        paramNode = fsm.getParamAtNode(node)
        compNode = OPNode("==", OPType.BINARY_EQ, currStateNode, paramNode)
        outName = node.name + "_ctrl_out"
        outNode = VarNode(outName)
        module.addPort(OutputPort(outNode, BasicRange(1)))
        module.addAssignment(Assignment(outNode, compNode))

    # generate the clk and reset ports
    clkNode = VarNode("clk")
    resetNode = VarNode("reset")
    module.addPort(InputPort(clkNode, BasicRange(1)))
    module.addPort(InputPort(resetNode, BasicRange(1)))

    # generate the start and finish ports
    startNode = VarNode("start")
    finishNode = VarNode("finish")
    module.addPort(InputPort(startNode, BasicRange(1)))
    module.addPort(OutputPort(finishNode, BasicRange(1)))


def fsm2module(fsm: FSM) -> Module:
    module = Module()
    nextStateNode, currStateNode = _fsmStateGeneration(fsm, module)
    _fsmStateTransitionGeneration(fsm, module, nextStateNode, currStateNode)
    _fsmCurrentStateAssignment(fsm, module, nextStateNode, currStateNode)
    _fsmInterfaceGeneration(fsm, module, nextStateNode, currStateNode)
    return module
