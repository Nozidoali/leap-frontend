from frontend import *
import os
import pytest
import pygraphviz as pgv

# change the working directory to the root directory of the project
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# test 00
# compatibility with legup
@pytest.mark.skip(reason="test takes too long")
def test_00_legup():
    verilogDir = "examples/verilogs/external/"
    verilogFile = os.path.join(verilogDir, "legup.v")
    netlist: Netlist = readVerilog(verilogFile)
    module: Module = netlist.getModuleAt(0)

    assert module is not None
    graph = exportDOT(module)
    graph.write("tmp.dot")


# test 01
# compatibility with Google XLS
@pytest.mark.skip(reason="not implemented")
def test_01_xls():
    verilogDir = "examples/verilogs/external/"
    verilogFile = os.path.join(verilogDir, "xls.v")
    netlist: Netlist = readVerilog(verilogFile)
    module: Module = netlist.getModuleAt(0)

    assert module is not None
    exportDOT(module)


# test 02
# compatibility with legup
@pytest.mark.skip(reason="test takes too long")
def test_02_legup():
    verilogDir = "examples/verilogs/external/"
    verilogFile = os.path.join(verilogDir, "legup2.v")
    netlist: Netlist = readVerilog(verilogFile)
    module: Module = netlist.getModuleAt(0)

    assert module is not None
    exportDOT(module)


# test 03
# compatibility with Vivado FSM
@pytest.mark.skip(reason="test takes too long")
def test_03_vivado():
    verilogDir = "examples/verilogs/external/"
    verilogFile = os.path.join(verilogDir, "vivado.v")
    netlist: Netlist = readVerilog(verilogFile)
    module: Module = netlist.getModuleAt(0)

    assert module is not None
    exportDOT(module)


if __name__ == "__main__":
    test_00_legup()
    # test_01_xls()
    # test_02_legup()
