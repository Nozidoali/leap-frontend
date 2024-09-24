from frontend import *
import os
import pytest

# change the working directory to the root directory of the project
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# test 00
# compatibility with legup
def test_00_legup():
    verilogDir = "examples/verilogs/external/"
    verilogFile = os.path.join(verilogDir, "legup.v")
    netlist: Netlist = readVerilog(verilogFile)
    module: Module = netlist.getModuleAt(0)

    assert module is not None
    module.exportDOT()
    module.writeDOT("tmp.dot")


# test 01
# compatibility with Google XLS
@pytest.mark.skip(reason="not implemented")
def test_01_xls():
    verilogDir = "examples/verilogs/external/"
    verilogFile = os.path.join(verilogDir, "xls.v")
    netlist: Netlist = readVerilog(verilogFile)
    module: Module = netlist.getModuleAt(0)

    assert module is not None
    module.exportDOT()
    module.writeDOT("tmp.dot")


# test 02
# compatibility with legup
def test_02_legup():
    verilogDir = "examples/verilogs/external/"
    verilogFile = os.path.join(verilogDir, "legup2.v")
    netlist: Netlist = readVerilog(verilogFile)
    module: Module = netlist.getModuleAt(0)

    assert module is not None
    module.exportDOT()
    module.writeDOT("tmp.dot")


if __name__ == "__main__":
    test_00_legup()
    # test_01_xls()
    test_02_legup()
