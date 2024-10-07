from frontend import *
import pytest


# Test 00
# Simple graph
def test_00_basic():
    graph = CFGraph()
    graph.addBB("A", 1, isStart=True)
    graph.addBB("B", 4)
    graph.addBB("C", 2, isFinish=True)

    graph.addFlow("A", "B")
    # B is a loop
    graph.addFlow("B", "B")
    graph.addFlow("B", "C")

    fsm = cfg2fsm(graph)

    assert len(fsm.nodes()) == 7
    assert len(fsm.edges()) == 7

    module = fsm2module(fsm)
    print(moduleToString(module))


# Test 01
# Simple graph
def test_01_basic():
    graph = CFGraph()
    graph.addBB("A", 1, isStart=True)
    graph.addBB("B", 4)
    graph.addBB("C", 3)
    graph.addBB("D", 3)
    graph.addBB("E", 2)
    graph.addBB("F", 1, isFinish=True)

    graph.addFlow("A", "B")

    # B is a loop with condition
    graph.addFlow("B", "C")
    graph.addFlow("B", "D")

    graph.addFlow("C", "E")
    graph.addFlow("D", "E")

    graph.addFlow("E", "B", isLoop=True, loopBound=10, loopII=3)

    # E is a loop with condition
    graph.addFlow("E", "F")

    fsm = cfg2fsm(graph)

    assert len(fsm.nodes()) == 14, f"len(fsm.nodes()) = {len(fsm.nodes())}"
    assert len(fsm.edges()) == 15, f"len(fsm.edges()) = {len(fsm.edges())}"

    module = fsm2module(fsm)
    job = Simulator(fsm)

    job.run()
    job.dumpGIF("tmp.gif")


if __name__ == "__main__":
    # test_00_basic()
    test_01_basic()
