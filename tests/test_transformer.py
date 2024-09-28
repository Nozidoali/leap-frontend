from frontend import *
import os
import pytest

# change the working directory to the root directory of the project
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_00_transformer():
    verilogDir = "examples/verilogs/grammars/"
    for file in os.listdir(verilogDir):
        if file.endswith(".v"):
            print(file)
            netlist: Netlist = readVerilog(verilogDir + file)
            module: Module = netlist.getModule("top")
            assert module is not None
            exportDOT(module)
    assert True


def write_after_read(data: str):
    netlist: Netlist = transformVerilogToNetlist(data)
    newData = netlistToString(netlist)
    print(newData)
    newNetlist: Netlist = transformVerilogToNetlist(newData)
    return netlist == newNetlist


# Test 01
# Basic Module Definition
def test_01_write_assignment():
    verilogString = """
module top(
        a,
        f,
        b
);
input  a;
input  b;
output  f;

assign f = a & b;
endmodule
    """
    assert write_after_read(verilogString)


# Test 02
# Port Range with constant
def test_02_write_assignment():
    verilogString = """
module top(
        a,
        f,
        b
);
`define WIDTH 8
input [`WIDTH-1:0] a;
input [`WIDTH-1:0] b;
output [`WIDTH-1:0] f;

assign f = a & b;
endmodule
    """
    assert write_after_read(verilogString)


if __name__ == "__main__":
    # test_00_transformer()
    test_02_write_assignment()
