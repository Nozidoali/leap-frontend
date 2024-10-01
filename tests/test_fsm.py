from frontend import *
import pytest


# Test 00
# Simple graph
def test_00_basic():
    graph = CFGraph()
    graph.addBB("A", 1)
    graph.addBB("B", 4)
    graph.addBB("C", 2)

    graph.addFlow("A", "B")

    # B is a loop
    graph.addFlow("B", "B")
    graph.addFlow("B", "C")

    fsm = cfg2fsm(graph)

    fsm.write("tmp.dot")


if __name__ == "__main__":
    test_00_basic()
