from frontend import *


def write_after_read(data: str):
    netlist: Netlist = transformVerilogToNetlist(data)
    newData = netlistToString(netlist)
    print(newData)
    newNetlist: Netlist = transformVerilogToNetlist(newData)
    return netlistsAreEqual(netlist, newNetlist)


# Test 00
# Basic Module Definition
def test_00_write_assignment():
    verilogString = """
module top(
        a,
        f,
        b
);
input  a;
input  b;
output  f;
endmodule
    """
    assert write_after_read(verilogString)


# Test 01
# Module Definition with bad port names
def test_01_write_assignment():
    verilogString = """
module top (
    input wire [3:0] a,
    input b,
    [1:0] c,
    d,
    output f
);
    output c;
    input [1:0] d;
endmodule
"""
    assert write_after_read(verilogString)


# Test 02
# Module Definition with bad port names
def test_02_write_assignment():
    verilogString = """
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
    assert write_after_read(verilogString)


# Test 03
# Basic assignment
def test_03_write_assignment():
    verilogString = """
module top (
    input wire [3:0] a,
    output f
);
    assign f = &a;
endmodule
"""
    assert write_after_read(verilogString)

# Test 04
# Basic assignment with expression
def test_04_write_assignment():
    verilogString = """
module top (
    input wire [3:0] a,
    output f
);
    assign f = &a ^ 1;
endmodule
"""
    assert write_after_read(verilogString)

# Test 05
# Basic assignment with Macro
def test_05_write_assignment():
    verilogString = """
module top (
    input wire [3:0] a,
    output f
);
    assign f = &a ^ `ONE;
endmodule
"""
    assert write_after_read(verilogString)


# Test 06
# Range with Macro
def test_06_write_assignment():
    verilogString = """
module top (
    input wire [`FOUR-1:0] a,
    output f
);
    assign f = &a ^ `ONE;
endmodule
"""
    assert write_after_read(verilogString)


if __name__ == "__main__":
    test_06_write_assignment()
