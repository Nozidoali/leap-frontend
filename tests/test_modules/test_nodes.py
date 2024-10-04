from frontend import *


# Test 00
# Simple node
def test_00_node():
    a = VarNode("a")
    assert a.name == "a"


# Test 01
# Simple node
def test_01_node():
    a = VarNode("a")
    assert a.isVariable() == True


# Test 02
# Simple node
def test_02_node():
    a = ConstantNode(1)
    assert a.isConstant() == True


# Test 03
# Simple node
def test_03_node():
    a = ConstantNode("1")
    assert a.isConstant() == True


# Test 04
# Simple node
def test_04_node():
    a = ConstantNode("1'b1")
    assert a.isConstant() == True


# Test 05
# Simple node
def test_05_node():
    a = ConstantNode("1'b1")
    assert a.isVariable() == False


# Test 06
# Simple node
def test_06_node():
    a = VarNode("a")
    assert a.isConstant() == False


# Test 07
# Variable node check
def test_07_node():
    a = VarNode("a")
    assert a.isVariable() == True


# Test 08
# Operation node with BINARY_ADD operator
def test_08_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("1"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_ADD


# Test 09
# Range handling
def test_09_node():
    r = BasicRange(4)
    a = VarNode("a", range=r)
    assert a.range.toWidth() == 4


# Test 10
# Copying node
def test_10_node():
    a = VarNode("a")
    b = a.copy()
    assert a.variable_name == b.variable_name


# Test 11
# Replacing variable in an operation node
def test_11_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("1"))
    assert a.children[0].variable_name == "a"
    assert a.children[1].isConstant() == True


# Test 12
# Operation node with BINARY_SUB operator
def test_12_node():
    a = OPNode("-", OPType.BINARY_SUB, VarNode("a"), ConstantNode("1"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_SUB


# Test 13
# Operation node with BINARY_MUL operator
def test_13_node():
    a = OPNode("*", OPType.BINARY_MUL, VarNode("a"), ConstantNode("2"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_MUL


# Test 14
# Operation node with BINARY_DIV operator
def test_14_node():
    a = OPNode("/", OPType.BINARY_DIV, VarNode("a"), ConstantNode("2"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_DIV


# Test 15
# Operation node with BINARY_AND operator
def test_15_node():
    a = OPNode("&", OPType.BINARY_AND, VarNode("a"), VarNode("b"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_AND


# Test 16
# Operation node with BINARY_OR operator
def test_16_node():
    a = OPNode("|", OPType.BINARY_OR, VarNode("a"), VarNode("b"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_OR


# Test 17
# Operation node with BINARY_XOR operator
def test_17_node():
    a = OPNode("^", OPType.BINARY_XOR, VarNode("a"), VarNode("b"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_XOR


# Test 18
# Operation node with UNARY_NOT operator (unary)
def test_18_node():
    a = OPNode("!", OPType.UNARY_NOT, VarNode("a"))
    assert a.isOperation() == True
    assert a.operation == OPType.UNARY_NOT


# Test 19
# Operation node with array indexing
def test_19_node():
    a = OPNode("[]", OPType.ARRAY_INDEX, VarNode("a"), ConstantNode("2"))
    assert a.isOperation() == True
    assert a.operation == OPType.ARRAY_INDEX


# Test 20
# Range node equality check
def test_20_node():
    r1 = BasicRange(4)
    r2 = BasicRange(4)
    assert r1 == r2


# Test 21
# Some events should be different
def test_21_event():
    a = seqEventNode()
    b = seqEventNode(useReset=True)
    assert a != b


# Test 22
# Some events should be different
def test_22_event():
    a = seqEventNode(useReset=True, customReset=VarNode("rst"))
    b = seqEventNode(useReset=True)
    assert a != b


# Test 23
# Some events should be the same
def test_23_event():
    a = seqEventNode(useReset=True, customReset=VarNode("rst"))
    b = seqEventNode(useReset=True, customReset=VarNode("rst"))
    assert a == b


# Test 24
# Some events should be the same
def test_24_event():
    a = combEventNode()
    b = combEventNode()
    assert a == b


# Test 25
# Some events should be the same
def test_25_event():
    a = seqEventNode()
    b = seqEventNode(customClk=VarNode("clk"))
    assert a == b


# Test 26
# Some events should be different
def test_26_event():
    a = seqEventNode()
    b = InitEvent()
    assert a != b


# Test 27
# test init event
def test_27_event():
    a = InitEvent()
    assert a.variable_name == "initial"


if __name__ == "__main__":
    # test_00_node()
    # test_01_node()
    # test_02_node()
    # test_03_node()
    # test_04_node()
    # test_05_node()
    # test_06_node()
    # test_08_node()
    # test_09_node()
    # test_10_node()
    # test_11_node()
    # test_12_node()
    # test_13_node()
    # test_14_node()
    # test_15_node()
    # test_16_node()
    # test_17_node()
    # test_18_node()
    # test_19_node()
    # test_20_node()
    # test_21_event()
    # test_22_event()
    # test_23_event()
    # test_24_event()
    # test_25_event()
    # test_26_event()
    test_27_event()
