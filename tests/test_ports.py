from frontend import *


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
    assert module.numInputs == 2, f"module.numInputs = {module.numInputs} != 2"
    assert module.numOutputs == 1, f"module.numOutputs = {module.numOutputs} != 1"


# Test 02
# Define a module with input, output, inout, and output ports
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
    assert module.numInputs == 3, f"module.numInputs = {module.numInputs} != 3"
    assert module.numOutputs == 2, f"module.numOutputs = {module.numOutputs} != 2"


# Test 03
# Define a module with input, output, inout, and output ports
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
    assert module.numInputs == 3, f"module.numInputs = {module.numInputs} != 3"
    assert module.numOutputs == 2, f"module.numOutputs = {module.numOutputs} != 2"


# Test 04
# Define a module with input, output, inout, and output ports
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
    input d;
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
    assert module.numInputs == 3, f"module.numInputs = {module.numInputs} != 3"
    assert module.numOutputs == 2, f"module.numOutputs = {module.numOutputs} != 2"


if __name__ == "__main__":
    test_00_basic()
    test_01_cornercases()
    test_02_case()
    test_03_case()
    test_04_case()
