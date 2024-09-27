from frontend import *
import pytest


# Test 01
# Define a module with a port defined as input and output
def test_00_false():
    verilogStr = """
module top (
    input a,
    output a
);
endmodule
"""
    with pytest.raises(AssertionError):
        netlist: Netlist = transformVerilogToNetlist(verilogStr)
        module: Module = netlist.getModule("top")
        assert module is not None


if __name__ == "__main__":
    test_00_false()
