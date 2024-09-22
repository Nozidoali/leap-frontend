from frontend import *
import os

# change the working directory to the root directory of the project
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_00_transformer():
    verilogDir = "examples/verilogs/grammars/"
    for file in os.listdir(verilogDir):
        if file.endswith(".v"):
            print(f"Testing {file}")
            netlist: Netlist = readVerilog(verilogDir + file)
            module: Module = netlist.getModule("top")
            assert module is not None
            module.exportDOT()
    assert True


if __name__ == "__main__":
    test_00_transformer()
