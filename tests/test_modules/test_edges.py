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


if __name__ == "__main__":
    test_00_assignment()
