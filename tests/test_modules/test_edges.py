from frontend import *
import pytest


# Test 00
# Simple graph
def test_00_assignment():
    a = VarNode("a")
    b = VarNode("b")

    assignment = BlockingAssignment(a, b)
    assert assignment.isBlocking == True


# Test 01
# non blocking assignment
def test_01_assignment():
    a = VarNode("a")
    b = VarNode("b")

    assignment = NonBlockingAssignment(a, b)
    assert assignment.isBlocking == False


# Test 02
# case assignment
def test_02_case_assignment():
    a = VarNode("a")
    b = VarNode("b")

    assignment = CaseAssignment(a, b, isBlocking=True)
    # assert assignment.isBlocking == False

    assignment.addCase(ConstantNode(1), Assignment(a, ConstantNode(1)))
    assignment.addCase(ConstantNode(0), Assignment(a, ConstantNode(0)))
    assignment.addCase(None, Assignment(a, ConstantNode(0)))
    print(assignment.toString())


# Test 03
# conditional assignment
def test_03_conditional_assignment():
    a = VarNode("a")
    b = VarNode("b")

    assignment = ConditionalAssignment(a, isBlocking=True)
    # assert assignment.isBlocking == False

    assignment.addBranch(ConstantNode(1), Assignment(a, ConstantNode(1)))
    assignment.addBranch(ConstantNode(0), Assignment(a, ConstantNode(0)))
    print(assignment.toString())


if __name__ == "__main__":
    # test_00_assignment()
    # test_02_case_assignment()
    test_03_conditional_assignment()
