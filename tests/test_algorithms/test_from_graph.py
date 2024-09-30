from frontend import *


# Test 00
# Simple graph to module
def test_00_basic():
    graph = CDFGraph()
    a = graph.addVarNode("a")
    b = graph.addVarNode("b")
    plus = graph.addOpNode("+", OPType.BINARY_ADD, [a, b])
    c = graph.addVarNode("c")
    graph.addAssignment(c, plus)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 2
    assert module.numOutputs == 1


if __name__ == "__main__":
    test_00_basic()
