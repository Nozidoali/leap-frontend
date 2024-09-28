from frontend import *

if __name__ == "__main__":
    netlist: Netlist = readVerilog("examples/verilogs/demo/simple.v")
    dot = exportDOT(netlist.getModuleAt(0))
    dot.write("output.dot")
    writeVerilog(netlist, "output.v")
