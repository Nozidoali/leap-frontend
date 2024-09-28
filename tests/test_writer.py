from frontend import *
import pytest


def write_after_read(data: str):
    netlist: Netlist = transformVerilogToNetlist(data)
    newData = netlistToString(netlist)
    print(newData)
    newNetlist: Netlist = transformVerilogToNetlist(newData)
    return netlist == newNetlist


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
@pytest.mark.skip(reason="not implemented")
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


# Test 07
# Expression Test Case 1
def test_07_write_expression():
    verilogString = """
module top (
    input wire [3:0] a,
    input wire [3:0] b,
    output f
);
    assign f = (&a) ^ b;
endmodule
"""
    assert write_after_read(verilogString)


# Test 08
# Binary Operator Test - AND, OR, XOR
def test_08_binary_operations():
    verilogString = """
module top (
    input wire [3:0] a,
    input wire [3:0] b,
    output wire f
);
    assign f = (a && b) || (a ^ b);
endmodule
"""
    assert write_after_read(verilogString)


# Test 09
# Unary Operator Test - NOT, INV
def test_09_unary_operations():
    verilogString = """
module top (
    input wire [3:0] a,
    output wire f
);
    assign f = !a | ~a;
endmodule
"""
    assert write_after_read(verilogString)


# Test 10
# Shift Operators - Left and Right Shift
def test_10_shift_operations():
    verilogString = """
module top (
    input wire [3:0] a,
    output wire f
);
    assign f = a << 2;
endmodule
"""
    assert write_after_read(verilogString)


# Test 11
# Array Concatenation
def test_11_array_concat():
    verilogString = """
module top (
    input wire [3:0] a,
    input wire [3:0] b,
    output wire [7:0] f
);
    assign f = {a, b};
endmodule
"""
    assert write_after_read(verilogString)


# Test 12
# Conditional Expression
def test_12_conditional_expression():
    verilogString = """
module top (
    input wire [3:0] a,
    input wire [3:0] b,
    output wire f
);
    assign f = (a > b) ? 1 : 0;
endmodule
"""
    assert write_after_read(verilogString)


# Test 13
# Multiple Binary Operations in a Single Expression
def test_13_multiple_operations():
    verilogString = """
module top (
    input wire [3:0] a,
    input wire [3:0] b,
    output wire f
);
    assign f = (a + b) - (a * b);
endmodule
"""
    assert write_after_read(verilogString)


# Test 14
# With if conditions
def test_14_conditions():
    verilogString = """
module top (
    input wire [3:0] a,
    input wire [3:0] b,
    output wire f
);
    if (a > b) begin
        assign f = 1;
    end else begin
        assign f = 0;
    end

endmodule
"""
    assert write_after_read(verilogString)


# Test 15
# Blocking and Non-Blocking Assignments
def test_15_conditions():
    verilogString = """
module top (
    input wire [3:0] a,
    input wire [3:0] b,
    output wire f,
    output reg g
);
    if (a > b) begin
        assign f = 1;
    end else begin
        assign f = 0;
    end
    
    if (a > b) begin
        g <= a;
    end else begin
        g <= b;
    end

endmodule
"""
    assert write_after_read(verilogString)


# Test 16
# Always event
def test_16_conditions():
    verilogString = """
module top (
    input wire clk,
    input wire [3:0] a,
    input wire [3:0] b,
    output wire f,
    output reg g
);

always @(posedge clk) begin
    if (a > b) begin
        assign f = 1;
    end else begin
        assign f = 0;
    end
    
    if (a > b) begin
        g <= a;
    end else begin
        g <= b;
    end
end
endmodule
"""
    assert write_after_read(verilogString)


# Test 17
# Always event
def test_17_conditions():
    verilogString = """
module top (
    input clk,
    input wire [3:0] a,
    input wire [3:0] b,
    output wire f,
    output reg g
);

always @(negedge clk) begin
    if (a > b) begin
        assign f = 1;
    end else begin
        assign f = 0;
    end
    
    if (a > b) begin
        g <= a;
    end else begin
        g <= b;
    end
end
endmodule
"""
    assert write_after_read(verilogString)


# Test 18
# Reset and positive edge clock event
def test_18_reset_event():
    verilogString = """
module top (
    input clk,
    input reset,
    input wire [3:0] a,
    input wire [3:0] b,
    output reg f
);

always @(posedge clk or posedge reset) begin
    if (reset) begin
        f <= 0;
    end else begin
        f <= a + b;
    end
end
endmodule
"""
    assert write_after_read(verilogString)


# Test 19
# Initial block with event-driven assignment
def test_19_initial_event():
    verilogString = """
module top (
    input wire [3:0] a,
    input wire [3:0] b,
    output reg f
);

initial begin
    f = 0;
end

always @(a or b) begin
    f <= a + b;
end
endmodule
"""
    assert write_after_read(verilogString)


# Test 20
# Always block with multiple conditions and mixed operators (and, or)
def test_20_mixed_event_conditions():
    verilogString = """
module top (
    input clk,
    input reset,
    input wire [3:0] a,
    input wire [3:0] b,
    output reg f
);

always @(posedge clk or negedge reset or a or b) begin
    if (!reset) begin
        f <= 0;
    end else if (a && b) begin
        f <= 1;
    end else if (a || b) begin
        f <= a + b;
    end else begin
        f <= 0;
    end
end
endmodule
"""
    assert write_after_read(verilogString)


# Test 21
# Mixed event-driven assignments with priority for * (wildcard)
def test_21_star_event():
    verilogString = """
module top (
    input wire [3:0] a,
    input wire [3:0] b,
    output reg f
);

always @(*) begin
    if (a == b) begin
        f <= 1;
    end else begin
        f <= 0;
    end
end
endmodule
"""
    assert write_after_read(verilogString)


# Test 22
# Multiple events combining and and or
@pytest.mark.skip(reason="not implemented")
def test_22_and_or_event():
    verilogString = """
module top (
    input clk,
    input wire [3:0] a,
    input wire [3:0] b,
    output reg f
);

always @(posedge clk or (a && b)) begin
    f <= (a && b) ? 1 : 0;
end
endmodule
"""
    assert write_after_read(verilogString)


# Test 23
# Parameters
def test_23_parameters():
    verilogString = """
`define WIDTH 4
module top (
    input wire [`WIDTH -1:0] a,
    input wire [`WIDTH -1:0] b,
    output wire [`WIDTH -1:0] f
);

assign f = a + b;
endmodule
"""
    assert write_after_read(verilogString)


# Test 24
# Timescale
def test_24_parameters():
    verilogString = """
`define WIDTH 4
`timescale 1ns / 1ps
module top (
    input wire [`WIDTH -1:0] a,
    input wire [`WIDTH -1:0] b,
    output wire [`WIDTH -1:0] f
);

assign f = a + b;
endmodule
"""
    assert write_after_read(verilogString)


# Test 25
# Parameters inside modules
def test_25_parameters():
    verilogString = """
module top (
    input wire a,
    input wire b,
    output wire f
);

`define WIDTH 4

wire [`WIDTH -1:0] a;
wire [`WIDTH -1:0] b;
wire [`WIDTH -1:0] f;

assign f = a + b;
endmodule
"""
    assert write_after_read(verilogString)


# Test 26
# Module instantiation
def test_26_module_instantiation():
    verilogString = """
module top (
    input wire a,
    input wire b,
    output wire f
);

add add_inst (
    .a(a),
    .b(b),
    .f(f)
);

defparam add_inst.WIDTH = 4;

endmodule
"""
    assert write_after_read(verilogString)


# Test 27
# Module instantiation
def test_27_module_instantiation():
    verilogString = """
module top (
    input wire a,
    input wire b,
    output wire f
);

add #(.WIDTH(4)) add_inst (
    .a(a),
    .b(b),
    .f(f)
);

endmodule
"""
    assert write_after_read(verilogString)


# Test 28
# Module instantiation
def test_28_module_instantiation():
    verilogString = """
module top (
    input wire a,
    input wire b,
    output wire f
);

add add_inst (
    .a(a),
    .b(b),
    .f(f)
);

defparam add_inst.IWIDTH = 4;
defparam add_inst.OWIDTH = 4;

endmodule
"""
    assert write_after_read(verilogString)


# Test 29
# Module instantiation
def test_29_module_instantiation():
    verilogString = """
module top (
    input wire a,
    input wire b,
    output wire f
);

add add_inst (
    .a(a),
    .b(b),
    .f(f)
);

defparam 
    add_inst.IWIDTH = 4,
    add_inst.OWIDTH = 4;

endmodule
"""
    assert write_after_read(verilogString)


# Test 30
# Port Type
def test_30_port_type():
    verilogString = """
module top (
    input wire a,
    input wire b,
    output reg f
);

always @(*) begin
    f = a + b;
end

endmodule
"""
    assert write_after_read(verilogString)


if __name__ == "__main__":
    # test_00_write_assignment()
    # test_01_write_assignment()
    # test_02_write_assignment()
    # test_03_write_assignment()
    # test_04_write_assignment()
    # test_05_write_assignment()
    # test_06_write_assignment()
    # test_07_write_expression()
    # test_08_binary_operations()
    # test_09_unary_operations()
    # test_10_shift_operations()
    # test_11_array_concat()
    # test_12_conditional_expression()
    # test_13_multiple_operations()
    # test_14_conditions()
    # test_15_conditions()
    # test_16_conditions()
    # test_17_conditions()
    # test_18_reset_event()
    # test_19_initial_event()
    # test_20_mixed_event_conditions()
    # test_21_star_event()
    # test_22_and_or_event()
    # test_23_parameters()
    # test_24_parameters()
    test_25_parameters()
    # test_26_module_instantiation()
    # test_27_module_instantiation()
    # test_28_module_instantiation()
    # test_29_module_instantiation()
    # test_30_port_type()
