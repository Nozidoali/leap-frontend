import math
from .graph import *


def _fsmStateGeneration(fsm: FSM, module: Module):
    assert len(fsm.nodes()) > 0, "FSM is empty"
    width: int = math.ceil(math.log2(len(fsm.nodes())))

    nextStateNode = VarNode("next_state")
    currStateNode = VarNode("curr_state")
    module.addPort(RegPort(nextStateNode, BasicRange(width)))
    module.addPort(WirePort(currStateNode, BasicRange(width)))
    for i, node in enumerate(fsm.nodes()):
        # we define each state as a parameter
        paramNode = fsm.getParamAtNode(node)
        module.addPort(ParameterPort(paramNode, BasicRange(width)))
        module.addAssignment(Assignment(paramNode, ConstantNode(f"3'd{i}")))
    return nextStateNode, currStateNode


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
    event = OPNode("always", OPType.EVENT_ALWAYS, OPNode("*", OPType.EVENT_COMB))
    assignment = CaseAssignment(nextStateNode, currStateNode, event=event)

    # add the state transition to enter the fsm using an input port start
    startNode = VarNode("start")
    module.addPort(InputPort(startNode, BasicRange(1)))

    for i, node in enumerate(fsm.nodes()):
        currParamNode = fsm.getParamAtNode(node)
        if len(fsm.successors(node)) == 0:
            continue
        elif len(fsm.successors(node)) == 1:
            succ = fsm.successors(node)[0]
            nextParamNode = fsm.getParamAtNode(succ)
            nextStateAssignment = Assignment(
                nextStateNode, nextParamNode, targetType=PortType.REG, isBlocking=True
            )
        else:
            conditionalAssignment = ConditionalAssignment(nextStateNode)
            for j, succ in enumerate(fsm.successors(node)[:-1]):
                controlNode = fsm.getControlSignalAtNode(succ, j)
                nextParamNode = fsm.getParamAtNode(succ)
                conditionalAssignment.addBranch(
                    controlNode,
                    Assignment(
                        nextStateNode,
                        nextParamNode,
                        targetType=PortType.REG,
                        isBlocking=True,
                    ),
                )
            # add a default case to the conditional assignment
            nextParamNode = fsm.getParamAtNode(fsm.successors(node)[-1])
            conditionalAssignment.addBranch(
                None,
                Assignment(
                    nextStateNode,
                    nextParamNode,
                    targetType=PortType.REG,
                    isBlocking=True,
                ),
            )
            nextStateAssignment = conditionalAssignment
        assignment.addCase(currParamNode, nextStateAssignment)
    # add a default case to the current state
    assert fsm.initialState is not None, "FSM has no initial state"
    initialStateNode = VarNode(fsm.initialState.name + "_label")
    assignment.addCase(
        None,
        Assignment(
            nextStateNode, initialStateNode, targetType=PortType.REG, isBlocking=True
        ),
    )
    # add the case assignment to the module
    module.addAssignment(assignment)


def _fsmInterfaceGeneration(fsm: FSM, module: Module, nextStateNode: VarNode, currStateNode: VarNode):
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


def fsm2module(fsm: FSM) -> Module:
    module = Module()
    nextStateNode, currStateNode = _fsmStateGeneration(fsm, module)
    _fsmStateTransitionGeneration(fsm, module, nextStateNode, currStateNode)

    _fsmInterfaceGeneration(fsm, module, nextStateNode, currStateNode)
    return module
