from frontend import *


# Test 00
# Simple module with input, output, and wire ports
def test_00_basic():
    verilogStr = """
module top (
    input a,
    input b,
    output f
);
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module is not None
    assert module.getPort("a").getType() == PortType.WIRE
    assert module.getPort("b").getType() == PortType.WIRE
    assert module.getPort("f").getType() == PortType.WIRE

    assert module.getPort("a").getDirection() == PortDirection.INPUT
    assert module.getPort("b").getDirection() == PortDirection.INPUT
    assert module.getPort("f").getDirection() == PortDirection.OUTPUT

    assert module.numInputs == 2, f"module.numInputs = {module.numInputs} != 2"
    assert module.numOutputs == 1, f"module.numOutputs = {module.numOutputs} != 1"


# Test 01
# Define a module with input, output, and wire ports
def test_01_cornercases():
    verilogStr = """
module top (
    input a,
    input b,
    output f
);
    wire w;
    assign w = a & b;
    assign f = w;
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module is not None
    assert module.getPort("a").getType() == PortType.WIRE
    assert module.getPort("b").getType() == PortType.WIRE
    assert module.getPort("f").getType() == PortType.WIRE

    assert module.getPort("a").getDirection() == PortDirection.INPUT
    assert module.getPort("b").getDirection() == PortDirection.INPUT
    assert module.getPort("f").getDirection() == PortDirection.OUTPUT

    assert module.numInputs == 2, f"module.numInputs = {module.numInputs} != 2"
    assert module.numOutputs == 1, f"module.numOutputs = {module.numOutputs} != 1"


# Test 02
# Define a module with mixed input and output ports
def test_02_case():
    verilogStr = """
module top (
    input a,
    input b,
    c,
    d,
    output f
);
    output c;
    input d;
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module is not None
    assert module.getPort("a").getType() == PortType.WIRE
    assert module.getPort("b").getType() == PortType.WIRE
    assert module.getPort("c").getType() == PortType.WIRE
    assert module.getPort("d").getType() == PortType.WIRE
    assert module.getPort("f").getType() == PortType.WIRE

    assert module.getPort("a").getDirection() == PortDirection.INPUT
    assert module.getPort("b").getDirection() == PortDirection.INPUT
    assert module.getPort("c").getDirection() == PortDirection.OUTPUT
    assert module.getPort("d").getDirection() == PortDirection.INPUT
    assert module.getPort("f").getDirection() == PortDirection.OUTPUT

    assert module.numInputs == 3, f"module.numInputs = {module.numInputs} != 3"
    assert module.numOutputs == 2, f"module.numOutputs = {module.numOutputs} != 2"


# Test 03
# Define a module with array and regular input/output ports
def test_03_case():
    verilogStr = """
module top (
    input wire [3:0] a,
    input b,
    [1:0] c,
    d,
    output f
);
    output c;
    input d;
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module is not None
    assert module.getPort("a").getType() == PortType.WIRE
    assert module.getPort("b").getType() == PortType.WIRE
    assert module.getPort("c").getType() == PortType.WIRE
    assert module.getPort("d").getType() == PortType.WIRE
    assert module.getPort("f").getType() == PortType.WIRE

    assert module.getPort("a").getDirection() == PortDirection.INPUT
    assert module.getPort("b").getDirection() == PortDirection.INPUT
    assert module.getPort("c").getDirection() == PortDirection.OUTPUT
    assert module.getPort("d").getDirection() == PortDirection.INPUT
    assert module.getPort("f").getDirection() == PortDirection.OUTPUT

    assert module.numInputs == 3, f"module.numInputs = {module.numInputs} != 3"
    assert module.numOutputs == 2, f"module.numOutputs = {module.numOutputs} != 2"


# Test 04
# Define a module with reg and wire signals
def test_04_case():
    verilogStr = """
module top (
    input wire [3:0] a,
    input b,
    [1:0] c,
    d,
    output f
);
    output c;
    input reg d;
    reg [3:0] e;
    wire [3:0] g;
    
    reg h [3:0];
    reg [3:0] i [3:0];
    
    wire [3:0] j [3:0];
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module is not None
    assert module.getPort("a").getType() == PortType.WIRE
    assert module.getPort("b").getType() == PortType.WIRE
    assert module.getPort("c").getType() == PortType.WIRE
    assert module.getPort("d").getType() == PortType.REG
    assert module.getPort("f").getType() == PortType.WIRE

    assert module.getPort("a").getDirection() == PortDirection.INPUT
    assert module.getPort("b").getDirection() == PortDirection.INPUT
    assert module.getPort("c").getDirection() == PortDirection.OUTPUT
    assert module.getPort("d").getDirection() == PortDirection.INPUT
    assert module.getPort("f").getDirection() == PortDirection.OUTPUT

    assert module.numInputs == 3, f"module.numInputs = {module.numInputs} != 3"
    assert module.numOutputs == 2, f"module.numOutputs = {module.numOutputs} != 2"


# Test 05
# Define a module where reg should not override input type
def test_05_port_type():
    verilogStr = """
module top (
    reg [3:0] a
);
    input a; /* This should not override the type of a */
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module.getPort("a").getType() == PortType.REG
    assert module.getPort("a").getDirection() == PortDirection.INPUT


# Test 06
# Define a module where reg should not override input type
def test_06_port_type():
    verilogStr = """
module top (
    input [3:0] a
);
    reg a; /* This should not override the type of a */
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module.getPort("a").getType() == PortType.REG
    assert module.getPort("a").getDirection() == PortDirection.INPUT


# Test 07:
# Define a wire internally
def test_07_port_type():
    verilogStr = """
module top (
);
    wire [3:0] a;
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module.getPort("a").getType() == PortType.WIRE


# Test 08:
# Define a module with integer port
def test_08_port_type():
    verilogStr = """
module top (
);
    integer a;
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module.getPort("a").getType() == PortType.INTEGER


# Test 09:
# Define a module with parameter port
def test_09_port_type():
    verilogStr = """
module top (
);
    parameter a = 4;
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module.getPort("a").getType() == PortType.PARAMETER


# Test 10:
# Define a module with localparam port
def test_10_port_type():
    verilogStr = """
module top (
);
    localparam a = 4;
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")
    assert module.getPort("a").getType() == PortType.LOCALPARAM


if __name__ == "__main__":
    test_00_basic()
    test_01_cornercases()
    test_02_case()
    test_03_case()
    test_04_case()
    test_05_port_type()
    test_06_port_type()
    test_07_port_type()
    test_08_port_type()
    test_09_port_type()
    test_10_port_type()
