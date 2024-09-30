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


# Test 01
# Unary operation
def test_01_unary():
    graph = CDFGraph()
    a = graph.addVarNode("a")
    neg = graph.addOpNode("-", OPType.UNARY_NEG, [a])
    b = graph.addVarNode("b")
    graph.addAssignment(b, neg)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 1
    assert module.numOutputs == 1


# Test 02
# Conditional expression
def test_02_conditional():
    graph = CDFGraph()
    cond = graph.addVarNode("cond")
    true_val = graph.addVarNode("true_val")
    false_val = graph.addVarNode("false_val")
    ternary = graph.addOpNode(
        "?:", OPType.CONDITIONAL_EXPRESSION, [cond, true_val, false_val]
    )
    out = graph.addVarNode("out")
    graph.addAssignment(out, ternary)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 3
    assert module.numOutputs == 1


# Test 03
# Logical AND
def test_03_logical_and():
    graph = CDFGraph()
    a = graph.addVarNode("a")
    b = graph.addVarNode("b")
    and_op = graph.addOpNode("&&", OPType.BINARY_AND, [a, b])
    c = graph.addVarNode("c")
    graph.addAssignment(c, and_op)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 2
    assert module.numOutputs == 1


# Test 04
# Array index
def test_04_array_index():
    graph = CDFGraph()
    arr = graph.addVarNode("arr")
    index = graph.addVarNode("index")
    array_idx = graph.addOpNode("[]", OPType.ARRAY_INDEX, [arr, index])
    out = graph.addVarNode("out")
    graph.addAssignment(out, array_idx)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 2
    assert module.numOutputs == 1


# Test 05
# Multiple operations
def test_05_multiple_ops():
    graph = CDFGraph()
    a = graph.addVarNode("a")
    b = graph.addVarNode("b")
    c = graph.addVarNode("c")

    add_op = graph.addOpNode("+", OPType.BINARY_ADD, [a, b])
    mul_op = graph.addOpNode("*", OPType.BINARY_MUL, [add_op, c])

    d = graph.addVarNode("d")
    graph.addAssignment(d, mul_op)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 3
    assert module.numOutputs == 1


if __name__ == "__main__":
    # test_00_basic()
    # test_01_unary()
    # test_02_conditional()
    # test_03_logical_and()
    # test_04_array_index()
    test_05_multiple_ops()
