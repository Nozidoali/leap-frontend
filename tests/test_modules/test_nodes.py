from frontend import *


# Test 00
# Simple node
def test_000_node():
    a = VarNode("a")
    assert a.name == "a"


# Test 01
# Simple node
def test_001_node():
    a = VarNode("a")
    assert a.isVariable() == True


# Test 02
# Simple node
def test_002_node():
    a = ConstantNode(1)
    assert a.isConstant() == True


# Test 03
# Simple node
def test_003_node():
    a = ConstantNode("1")
    assert a.isConstant() == True


# Test 04
# Simple node
def test_004_node():
    a = ConstantNode("1'b1")
    assert a.isConstant() == True


# Test 05
# Simple node
def test_005_node():
    a = ConstantNode("1'b1")
    assert a.isVariable() == False


# Test 06
# Simple node
def test_006_node():
    a = VarNode("a")
    assert a.isConstant() == False


# Test 07
# Variable node check
def test_007_node():
    a = VarNode("a")
    assert a.isVariable() == True


# Test 08
# Operation node with BINARY_ADD operator
def test_008_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("1"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_ADD


# Test 09
# Range handling
def test_009_node():
    r = BasicRange(4)
    a = VarNode("a", range=r)
    assert a.range.toWidth() == 4


# Test 10
# Copying node
def test_010_node():
    a = VarNode("a")
    b = a.copy()
    assert a.variable_name == b.variable_name


# Test 11
# Replacing variable in an operation node
def test_011_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("1"))
    assert a.children[0].variable_name == "a"
    assert a.children[1].isConstant() == True


# Test 12
# Operation node with BINARY_SUB operator
def test_012_node():
    a = OPNode("-", OPType.BINARY_SUB, VarNode("a"), ConstantNode("1"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_SUB


# Test 13
# Operation node with BINARY_MUL operator
def test_013_node():
    a = OPNode("*", OPType.BINARY_MUL, VarNode("a"), ConstantNode("2"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_MUL


# Test 14
# Operation node with BINARY_DIV operator
def test_014_node():
    a = OPNode("/", OPType.BINARY_DIV, VarNode("a"), ConstantNode("2"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_DIV


# Test 15
# Operation node with BINARY_AND operator
def test_015_node():
    a = OPNode("&", OPType.BINARY_AND, VarNode("a"), VarNode("b"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_AND


# Test 16
# Operation node with BINARY_OR operator
def test_016_node():
    a = OPNode("|", OPType.BINARY_OR, VarNode("a"), VarNode("b"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_OR


# Test 17
# Operation node with BINARY_XOR operator
def test_017_node():
    a = OPNode("^", OPType.BINARY_XOR, VarNode("a"), VarNode("b"))
    assert a.isOperation() == True
    assert a.operation == OPType.BINARY_XOR


# Test 18
# Operation node with UNARY_NOT operator (unary)
def test_018_node():
    a = OPNode("!", OPType.UNARY_NOT, VarNode("a"))
    assert a.isOperation() == True
    assert a.operation == OPType.UNARY_NOT


# Test 19
# Operation node with array indexing
def test_019_node():
    a = OPNode("[]", OPType.ARRAY_INDEX, VarNode("a"), ConstantNode("2"))
    assert a.isOperation() == True
    assert a.operation == OPType.ARRAY_INDEX


# Test 20
# Range node equality check
def test_020_node():
    r1 = BasicRange(4)
    r2 = BasicRange(4)
    assert r1 == r2


# Test 21
# Some events should be different
def test_021_event():
    a = seqEventNode()
    b = seqEventNode(useReset=True)
    assert a != b


# Test 22
# Some events should be different
def test_022_event():
    a = seqEventNode(useReset=True, customReset=VarNode("rst"))
    b = seqEventNode(useReset=True)
    assert a != b


# Test 23
# Some events should be the same
def test_023_event():
    a = seqEventNode(useReset=True, customReset=VarNode("rst"))
    b = seqEventNode(useReset=True, customReset=VarNode("rst"))
    assert a == b


# Test 24
# Some events should be the same
def test_024_event():
    a = combEventNode()
    b = combEventNode()
    assert a == b


# Test 25
# Some events should be the same
def test_025_event():
    a = seqEventNode()
    b = seqEventNode(customClk=VarNode("clk"))
    assert a == b


# Test 26
# Some events should be different
def test_026_event():
    a = seqEventNode()
    b = InitEvent()
    assert a != b


# Test 27
# test init event
def test_027_event():
    a = InitEvent()
    assert a.variable_name == "initial"


# Test 28
# Test operation node string representation with unary operation
def test_028_node():
    a = OPNode("!", OPType.UNARY_NOT, VarNode("a"))
    assert a.toString() == "! a"


# Test 29
# Test operation node string representation with binary operation
def test_029_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("5"))
    assert a.toString() == "a + 5"


# Test 30
# Test operation node string representation with unary operation
def test_030_node():
    a = OPNode("!", OPType.UNARY_NOT, VarNode("a"))
    assert a.toString() == "! a"


# Test 31
# Test node replacement within operation node
def test_031_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("1"))
    a.replaceVariable("a", "b")
    assert a.children[0].variable_name == "b"


# Test 32
# Test range width calculation
def test_032_node():
    r = BasicRange(8)
    a = VarNode("data", range=r)
    assert a.range.toWidth() == 8


# Test 33
# Test operation node with ARRAY_SLICE
def test_033_node():
    a = OPNode(
        "[]", OPType.ARRAY_SLICE, VarNode("data"), ConstantNode("3"), ConstantNode("0")
    )
    assert a.isOperation() == True
    assert a.operation == OPType.ARRAY_SLICE


# Test 34
# Test array concatenation operation
def test_034_node():
    a = OPNode("{}", OPType.ARRAY_CONCAT, VarNode("a"), VarNode("b"))
    assert a.isOperation() == True
    assert a.operation == OPType.ARRAY_CONCAT


# Test 35
# Test multiple operation nodes with precedence and associativity
def test_035_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("1"))
    b = OPNode("*", OPType.BINARY_MUL, VarNode("b"), a)
    assert b.toString() == "b * (a + 1)"


# Test 36
# Test constant node string representation
def test_036_node():
    a = ConstantNode("32'hFFFF_FFFF")
    assert a.toString() == "32'hFFFF_FFFF"


# Test 37
# Test range equality for non-equal ranges
def test_037_node():
    r1 = BasicRange(8)
    r2 = BasicRange(4)
    assert r1 != r2


# Test 38
# Test variable replacement in an array index operation
def test_038_node():
    a = OPNode("[]", OPType.ARRAY_INDEX, VarNode("a"), ConstantNode("3"))
    a.replaceVariable("a", "b")
    assert a.children[0].variable_name == "b"


# Test 39
# Test copying an operation node
def test_039_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("1"))
    b = a.copy()
    assert b.operation == a.operation
    assert b.children[0].variable_name == a.children[0].variable_name


# Test 40
# Test event node string representation
def test_040_event():
    a = seqEventNode(
        customClk=VarNode("clk"), useReset=True, customReset=VarNode("rst")
    )
    assert a.toString() == "always @(posedge clk or posedge rst)"


# Test 41
# Test event node without reset
def test_041_event():
    a = seqEventNode(customClk=VarNode("clk"))
    assert a.toString() == "always @(posedge clk)"


# Test 42
# Copying a VarNode
def test_042_node():
    a = VarNode("signal")
    b = a.copy()
    assert a.variable_name == b.variable_name
    assert a is not b  # Ensure that it's a deep copy


# Test 43
# Copying a ConstantNode
def test_043_node():
    a = ConstantNode("32'hDEADBEEF")
    b = a.copy()
    assert a.variable_name == b.variable_name
    assert a is not b  # Ensure that it's a deep copy


# Test 44
# Copying a binary operation node
def test_044_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("x"), ConstantNode("4"))
    b = a.copy()
    assert a.operation == b.operation
    assert a.children[0].variable_name == b.children[0].variable_name
    assert a.children[1].variable_name == b.children[1].variable_name
    assert a is not b  # Ensure that it's a deep copy


# Test 45
# Copying a unary operation node
def test_045_node():
    a = OPNode("!", OPType.UNARY_NOT, VarNode("flag"))
    b = a.copy()
    assert a.operation == b.operation
    assert a.children[0].variable_name == b.children[0].variable_name
    assert a is not b  # Ensure that it's a deep copy


# Test 46
# Copying a node with a range
def test_046_node():
    r = BasicRange(16)
    a = VarNode("data", range=r)
    b = a.copy()
    assert a.variable_name == b.variable_name
    assert a.range.toWidth() == b.range.toWidth()
    assert a is not b  # Ensure that it's a deep copy


# Test 47
# Copying a complex operation node (nested binary and unary ops)
def test_047_node():
    a = OPNode(
        "+",
        OPType.BINARY_ADD,
        OPNode("!", OPType.UNARY_NOT, VarNode("x")),
        ConstantNode("10"),
    )
    b = a.copy()
    assert a.operation == b.operation
    assert a.children[0].operation == b.children[0].operation
    assert a.children[1].variable_name == b.children[1].variable_name
    assert a is not b  # Ensure deep copy


# Test 48
# Copying an event node
def test_048_event():
    a = seqEventNode(
        customClk=VarNode("clk"), useReset=True, customReset=VarNode("rst")
    )
    b = a.copy()
    assert a == b
    assert a is not b  # Ensure deep copy


# Test 49
# Copying an array operation node
def test_049_node():
    a = OPNode("[]", OPType.ARRAY_INDEX, VarNode("arr"), ConstantNode("2"))
    b = a.copy()
    assert a.operation == b.operation
    assert a.children[0].variable_name == b.children[0].variable_name
    assert a.children[1].variable_name == b.children[1].variable_name
    assert a is not b  # Ensure deep copy


# Test 50
# Copying an array concatenation operation node
def test_050_node():
    a = OPNode("{}", OPType.ARRAY_CONCAT, VarNode("a"), VarNode("b"))
    b = a.copy()
    assert a.operation == b.operation
    assert a.children[0].variable_name == b.children[0].variable_name
    assert a.children[1].variable_name == b.children[1].variable_name
    assert a is not b  # Ensure deep copy


# Test 51
# Copying a node with multiple nested children
def test_051_node():
    a = OPNode(
        "*",
        OPType.BINARY_MUL,
        OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("3")),
        ConstantNode("5"),
    )
    b = a.copy()
    assert a.operation == b.operation
    assert a.children[0].operation == b.children[0].operation
    assert a.children[1].variable_name == b.children[1].variable_name
    assert (
        a.children[0].children[0].variable_name
        == b.children[0].children[0].variable_name
    )
    assert (
        a.children[0].children[1].variable_name
        == b.children[0].children[1].variable_name
    )
    assert a is not b  # Ensure deep copy


# Test 52
# Copying a range node
def test_052_node():
    r1 = BasicRange(4)
    r2 = r1.copy()
    assert r1.toWidth() == r2.toWidth()
    assert r1 is not r2  # Ensure deep copy


# Test 53
# Copying a node and changing the copy
def test_053_node():
    a = VarNode("a")
    b = a.copy()
    b.variable_name = "b"
    assert a.variable_name == "a"
    assert b.variable_name == "b"


# Test 54
# Copying an event node and modifying the copy
def test_054_event():
    a = seqEventNode(
        customClk=VarNode("clk"), useReset=True, customReset=VarNode("rst")
    )
    b = a.copy()
    assert a.variable_name == b.variable_name
    assert a == b


# Test 55
# Equality check for two identical VarNodes
def test_055_node():
    a = VarNode("signal")
    b = VarNode("signal")
    assert a == b


# Test 56
# Equality check for two different VarNodes
def test_056_node():
    a = VarNode("signal1")
    b = VarNode("signal2")
    assert a != b


# Test 57
# Equality check for two identical ConstantNodes
def test_057_node():
    a = ConstantNode("32'h1A2B3C4D")
    b = ConstantNode("32'h1A2B3C4D")
    assert a == b


# Test 58
# Equality check for two different ConstantNodes
def test_058_node():
    a = ConstantNode("32'h1A2B3C4D")
    b = ConstantNode("32'h4D3C2B1A")
    assert a != b


# Test 59
# Equality check for two identical operation nodes with same structure
def test_059_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("x"), ConstantNode("5"))
    b = OPNode("+", OPType.BINARY_ADD, VarNode("x"), ConstantNode("5"))
    assert a == b


# Test 60
# Equality check for two different operation nodes
def test_060_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("x"), ConstantNode("5"))
    b = OPNode("-", OPType.BINARY_SUB, VarNode("x"), ConstantNode("5"))
    assert a != b


# Test 61
# Equality check for operation nodes with different children
def test_061_node():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("x"), ConstantNode("5"))
    b = OPNode("+", OPType.BINARY_ADD, VarNode("y"), ConstantNode("5"))
    assert a != b


# Test 62
# Equality check for identical event nodes
def test_062_event():
    a = seqEventNode(customClk=VarNode("clk"), useReset=True)
    b = seqEventNode(customClk=VarNode("clk"), useReset=True)
    assert a == b


# Test 63
# Equality check for event nodes with different clocks
def test_063_event():
    a = seqEventNode(customClk=VarNode("clk"), useReset=True)
    b = seqEventNode(customClk=VarNode("reset"), useReset=True)
    assert a != b


# Test 64
# Equality check for event nodes with different reset conditions
def test_064_event():
    a = seqEventNode(useReset=True, customReset=VarNode("rst"))
    b = seqEventNode(useReset=True)
    assert a != b


# Test 65
# Equality check for operation node with array index and same structure
def test_065_node():
    a = OPNode("[]", OPType.ARRAY_INDEX, VarNode("arr"), ConstantNode("2"))
    b = OPNode("[]", OPType.ARRAY_INDEX, VarNode("arr"), ConstantNode("2"))
    assert a == b


# Test 66
# Equality check for operation node with array index and different children
def test_066_node():
    a = OPNode("[]", OPType.ARRAY_INDEX, VarNode("arr"), ConstantNode("2"))
    b = OPNode("[]", OPType.ARRAY_INDEX, VarNode("arr"), ConstantNode("3"))
    assert a != b


# Test 67
# Equality check for two identical range nodes
def test_067_range():
    r1 = BasicRange(8)
    r2 = BasicRange(8)
    assert r1 == r2


# Test 68
# Equality check for two different range nodes
def test_068_range():
    r1 = BasicRange(8)
    r2 = BasicRange(16)
    assert r1 != r2


# Test 69
# Equality check for different nested operation nodes
def test_069_node():
    a = OPNode(
        "*",
        OPType.BINARY_MUL,
        OPNode("+", OPType.BINARY_ADD, VarNode("x"), ConstantNode("5")),
        ConstantNode("2"),
    )
    b = OPNode(
        "*",
        OPType.BINARY_MUL,
        OPNode("+", OPType.BINARY_ADD, VarNode("y"), ConstantNode("5")),
        ConstantNode("2"),
    )
    assert a != b


# Test 70
# Equality check for two InitEvent nodes with the same attributes
def test_070_event():
    a = InitEvent()
    b = InitEvent()
    assert a == b


# Test 72
# toString for a simple ConstantNode
def test_072_constant_node():
    a = ConstantNode("32'h1A2B3C4D")
    assert a.toString() == "32'h1A2B3C4D"


# Test 73
# toString for a simple VarNode
def test_073_var_node():
    a = VarNode("signal")
    assert a.toString() == "signal"


# Test 74
# toString for a simple OPNode with a binary addition
def test_074_op_node_addition():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("1"))
    assert a.toString() == "a + 1"


# Test 75
# toString for a simple OPNode with a binary subtraction
def test_075_op_node_subtraction():
    a = OPNode("-", OPType.BINARY_SUB, VarNode("a"), ConstantNode("1"))
    assert a.toString() == "a - 1"


# Test 76
# toString for a binary multiplication operation
def test_076_op_node_multiplication():
    a = OPNode("*", OPType.BINARY_MUL, VarNode("a"), ConstantNode("2"))
    assert a.toString() == "a * 2"


# Test 77
# toString for a binary division operation
def test_077_op_node_division():
    a = OPNode("/", OPType.BINARY_DIV, VarNode("a"), ConstantNode("2"))
    assert a.toString() == "a / 2"


# Test 78
# toString for a binary AND operation
def test_078_op_node_and():
    a = OPNode("&", OPType.BINARY_AND, VarNode("a"), VarNode("b"))
    assert a.toString() == "a & b"


# Test 79
# toString for a binary OR operation
def test_079_op_node_or():
    a = OPNode("|", OPType.BINARY_OR, VarNode("a"), VarNode("b"))
    assert a.toString() == "a | b"


# Test 80
# toString for a binary XOR operation
def test_080_op_node_xor():
    a = OPNode("^", OPType.BINARY_XOR, VarNode("a"), VarNode("b"))
    assert a.toString() == "a ^ b"


# Test 81
# toString for a unary NOT operation
def test_081_op_node_unary_not():
    a = OPNode("!", OPType.UNARY_NOT, VarNode("a"))
    assert a.toString() == "! a"


# Test 82
# toString for an array index operation
def test_082_op_node_array_index():
    a = OPNode("[]", OPType.ARRAY_INDEX, VarNode("array"), ConstantNode("2"))
    assert a.toString() == "array[2]"


# Test 83
# toString for a nested operation node
# NOTE: the parantheses are not necessary if the operation has higher precedence
def test_083_nested_op_node():
    a = OPNode(
        "+",
        OPType.BINARY_ADD,
        OPNode("*", OPType.BINARY_MUL, VarNode("a"), ConstantNode("2")),
        ConstantNode("3"),
    )
    assert a.toString() == "a * 2 + 3"


# Test 84
# toString for a more complex nested operation node
def test_084_complex_nested_op_node():
    a = OPNode(
        "+",
        OPType.BINARY_ADD,
        OPNode(
            "*",
            OPType.BINARY_MUL,
            OPNode("-", OPType.BINARY_SUB, VarNode("x"), ConstantNode("5")),
            VarNode("y"),
        ),
        ConstantNode("10"),
    )
    assert a.toString() == "(x - 5) * y + 10"


# Test 85
# toString for an event node
def test_085_event_node():
    a = seqEventNode(customClk=VarNode("clk"), useReset=True)
    assert a.toString() == "always @(posedge clk or posedge reset)"


# Test 86
# toString for an InitEvent
def test_086_init_event():
    a = InitEvent()
    assert a.toString() == "initial"


# Test 87
# toString for a copy of a ConstantNode
def test_087_constant_copy():
    a = ConstantNode("32'h1A2B3C4D")
    b = a.copy()
    assert b.toString() == a.toString()


# Test 88
# toString for a copy of a VarNode
def test_088_var_copy():
    a = VarNode("signal")
    b = a.copy()
    assert b.toString() == a.toString()


# Test 89
# toString for a copy of an OPNode
def test_089_op_copy():
    a = OPNode("+", OPType.BINARY_ADD, VarNode("x"), ConstantNode("5"))
    b = a.copy()
    assert b.toString() == a.toString()


# Test 90
# toString for a copy of a nested OPNode
def test_090_nested_op_copy():
    a = OPNode(
        "+",
        OPType.BINARY_ADD,
        OPNode("*", OPType.BINARY_MUL, VarNode("a"), ConstantNode("2")),
        ConstantNode("3"),
    )
    b = a.copy()
    assert b.toString() == a.toString()


# Test 91
# toString for an event node with a custom reset
def test_091_event_node_with_reset():
    a = seqEventNode(
        customClk=VarNode("clk"), useReset=True, customReset=VarNode("rst")
    )
    assert a.toString() == "always @(posedge clk or posedge rst)"


# Test 92
# toString for a complex assignment involving variables and operations
def test_092_assignment_to_operation():
    a = Assignment(
        VarNode("result"),
        OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("2")),
    )
    assert a.toString() == "assign result = a + 2;\n"


# Test 93
# toString for a blocking assignment
def test_093_blocking_assignment():
    a = BlockingAssignment(VarNode("result"), ConstantNode("0"))
    assert a.toString() == "assign result = 0;\n"


# Test 94
# toString for a non-blocking assignment
def test_094_non_blocking_assignment():
    a = NonBlockingAssignment(
        VarNode("result"),
        OPNode("*", OPType.BINARY_MUL, VarNode("a"), ConstantNode("2")),
    )
    assert a.toString() == "assign result <= a * 2;\n"


# Test 95
# toString for a reg assignment
def test_095_reg_assignment():
    a = RegAssignment(VarNode("result"), ConstantNode("0"))
    assert a.toString() == "result <= 0;\n"


# Test 96
# toString for a wire assignment
def test_096_wire_assignment():
    a = WireAssignment(
        VarNode("result"),
        OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("2")),
    )
    assert a.toString() == "assign result = a + 2;\n"


# Test 97
# toString for a latch assignment
def test_097_latch_assignment():
    a = LatchAssignment(
        VarNode("result"),
        OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("2")),
    )
    assert a.toString() == "result = a + 2;\n"


# Test 98
# Equality check for two different event nodes
def test_098_event_equality():
    event1 = seqEventNode(customClk=VarNode("clk"))
    event2 = seqEventNode(customClk=VarNode("clk"))
    assert event1 == event2


# Test 99
# Inequality check for two different event nodes
def test_099_event_inequality():
    event1 = seqEventNode(customClk=VarNode("clk"))
    event2 = seqEventNode(customClk=VarNode("reset"))
    assert event1 != event2


# Test 100
# Equality check for two identical InitEvents
def test_100_init_event_equality():
    init_event1 = InitEvent()
    init_event2 = InitEvent()
    assert init_event1 == init_event2


# Test 101
# Inequality check for an InitEvent and a regular event node
def test_101_event_and_init_event_inequality():
    event1 = seqEventNode(customClk=VarNode("clk"))
    init_event = InitEvent()
    assert event1 != init_event


# Test 102
# Equality check for two identical VarNodes
def test_102_var_node_equality():
    var1 = VarNode("x")
    var2 = VarNode("x")
    assert var1 == var2


# Test 103
# Inequality check for two different VarNodes
def test_103_var_node_inequality():
    var1 = VarNode("x")
    var2 = VarNode("y")
    assert var1 != var2


# Test 104
# Equality check for two identical ConstantNodes
def test_104_constant_node_equality():
    const1 = ConstantNode("32'h1A2B3C4D")
    const2 = ConstantNode("32'h1A2B3C4D")
    assert const1 == const2


# Test 105
# Inequality check for two different ConstantNodes
def test_105_constant_node_inequality():
    const1 = ConstantNode("32'h1A2B3C4D")
    const2 = ConstantNode("32'h2B3C4D5E")
    assert const1 != const2


# Test 106
# Equality check for two identical OPNodes
def test_106_op_node_equality():
    op1 = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("2"))
    op2 = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("2"))
    assert op1 == op2


# Test 107
# Inequality check for two different OPNodes
def test_107_op_node_inequality():
    op1 = OPNode("+", OPType.BINARY_ADD, VarNode("a"), ConstantNode("2"))
    op2 = OPNode("-", OPType.BINARY_SUB, VarNode("a"), ConstantNode("2"))
    assert op1 != op2


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
