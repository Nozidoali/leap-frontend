from frontend import *
import pytest
import lark


# Test 00
# Define a module with a port defined as input and output
def test_00_false():
    verilogStr = """
module top (
    input a,
    output a
);
endmodule
"""
    with pytest.raises(lark.exceptions.VisitError):
        netlist: Netlist = transformVerilogToNetlist(verilogStr)
        module: Module = netlist.getModule("top")
        assert module is not None


# Test 01
# Define a module with a port defined as wire and reg
def test_01_false():
    verilogStr = """
module top (
    input wire a
);
reg a;
endmodule
"""
    with pytest.raises(lark.exceptions.VisitError):
        netlist: Netlist = transformVerilogToNetlist(verilogStr)
        module: Module = netlist.getModule("top")
        assert module is not None


# Test 02
# Define a module with a port defined as different ranges
def test_02_false():
    verilogStr = """
module top (
    input [3:0] a
);
    reg [2:0] a;
endmodule
"""
    with pytest.raises(lark.exceptions.VisitError):
        netlist: Netlist = transformVerilogToNetlist(verilogStr)
        module: Module = netlist.getModule("top")
        assert module is not None


if __name__ == "__main__":
    test_00_false()
    test_01_false()
    test_02_false()
