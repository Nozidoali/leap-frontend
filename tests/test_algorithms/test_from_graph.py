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


# Test 06
# Simple graph to module with range
def test_06_basic():
    graph = CDFGraph()
    a = graph.addVarNode("a", BasicRange(8))
    b = graph.addVarNode("b", BasicRange(8))
    plus = graph.addOpNode("+", OPType.BINARY_ADD, [a, b])
    c = graph.addVarNode("c", BasicRange(8))
    graph.addAssignment(c, plus)
    graph.write("output.dot")
    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 2
    assert module.numOutputs == 1

    # Check the ranges
    assert module.getPort("a").range == BasicRange(8)
    assert module.getPort("b").range == BasicRange(8)
    assert module.getPort("c").range == BasicRange(8)


# Test 07
# Unary operation with range
def test_07_unary():
    graph = CDFGraph()
    a = graph.addVarNode("a", BasicRange(8))
    neg = graph.addOpNode("-", OPType.UNARY_NEG, [a])
    b = graph.addVarNode("b", BasicRange(8))
    graph.addAssignment(b, neg)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 1
    assert module.numOutputs == 1

    # Check the ranges
    assert module.getPort("a").range == BasicRange(8)
    assert module.getPort("b").range == BasicRange(8)


# Test 08
# Conditional expression with range
def test_08_conditional():
    graph = CDFGraph()
    cond = graph.addVarNode("cond", BasicRange(1))
    true_val = graph.addVarNode("true_val", BasicRange(8))
    false_val = graph.addVarNode("false_val", BasicRange(8))
    ternary = graph.addOpNode(
        "?:", OPType.CONDITIONAL_EXPRESSION, [cond, true_val, false_val]
    )
    out = graph.addVarNode("out", BasicRange(8))
    graph.addAssignment(out, ternary)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 3
    assert module.numOutputs == 1

    # Check the ranges
    assert module.getPort("cond").range == BasicRange(1)
    assert module.getPort("true_val").range == BasicRange(8)
    assert module.getPort("false_val").range == BasicRange(8)
    assert module.getPort("out").range == BasicRange(8)


# Test 09
# Logical AND with range
def test_09_logical_and():
    graph = CDFGraph()
    a = graph.addVarNode("a", BasicRange(1))
    b = graph.addVarNode("b", BasicRange(1))
    and_op = graph.addOpNode("&&", OPType.BINARY_AND, [a, b])
    c = graph.addVarNode("c", BasicRange(1))
    graph.addAssignment(c, and_op)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 2
    assert module.numOutputs == 1

    # Check the ranges
    assert module.getPort("a").range == BasicRange(1)
    assert module.getPort("b").range == BasicRange(1)
    assert module.getPort("c").range == BasicRange(1)


# Test 10
# Array index with range
def test_10_array_index():
    graph = CDFGraph()
    arr = graph.addVarNode("arr", BasicRange(32))
    index = graph.addVarNode("index", BasicRange(5))  # Assuming 5-bit index
    array_idx = graph.addOpNode("[]", OPType.ARRAY_INDEX, [arr, index])
    out = graph.addVarNode("out", BasicRange(1))  # Assuming single-bit output
    graph.addAssignment(out, array_idx)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 2
    assert module.numOutputs == 1

    # Check the ranges
    assert module.getPort("arr").range == BasicRange(32)
    assert module.getPort("index").range == BasicRange(5)
    assert module.getPort("out").range == BasicRange(1)


# Test 11
# Multiple operations with range
def test_11_multiple_ops():
    graph = CDFGraph()
    a = graph.addVarNode("a", BasicRange(8))
    b = graph.addVarNode("b", BasicRange(8))
    c = graph.addVarNode("c", BasicRange(8))

    add_op = graph.addOpNode("+", OPType.BINARY_ADD, [a, b])
    mul_op = graph.addOpNode("*", OPType.BINARY_MUL, [add_op, c])

    d = graph.addVarNode("d", BasicRange(16))  # Assuming the output is 16 bits
    graph.addAssignment(d, mul_op)

    module = graphToModule(graph)

    # Check the module
    print(moduleToString(module))
    assert module.numInouts == 0
    assert module.numInputs == 3
    assert module.numOutputs == 1

    # Check the ranges
    assert module.getPort("a").range == BasicRange(8)
    assert module.getPort("b").range == BasicRange(8)
    assert module.getPort("c").range == BasicRange(8)
    assert module.getPort("d").range == BasicRange(16)


if __name__ == "__main__":
    # test_00_basic()
    # test_01_unary()
    # test_02_conditional()
    # test_03_logical_and()
    # test_04_array_index()
    # test_05_multiple_ops()
    test_06_basic()
