from frontend import *
import pytest


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
    with pytest.raises(ValueError):
        transformVerilogToNetlist(verilogStr)


# Test 01
# Define a module with input, output, and wire ports
def test_01_cornercases():
    verilogStr = """
module top (
    input a,
    input b,
    output f
);
assign a = b + 1;
endmodule
"""
    with pytest.raises(ValueError):
        transformVerilogToNetlist(verilogStr)


# Test 02
# Define a module with input, output, and wire ports
def test_02_cornercases():
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
    
    assign f = d;
endmodule
"""
    with pytest.raises(ValueError):
        transformVerilogToNetlist(verilogStr)


# Test 03
# Define a module with input, output, and wire ports
def test_03_cornercases():
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
    
    assign c = a & b;
endmodule
"""
    with pytest.raises(ValueError):
        transformVerilogToNetlist(verilogStr)


if __name__ == "__main__":
    # test_00_basic()
    test_01_cornercases()
