from frontend import *

if __name__ == "__main__":
    netlist: Netlist = readVerilog("examples/verilogs/external/legup.v")
    dotOld = moduleToGraph(netlist.getModuleAt(0))
    dotOld.write("output.dot")
    dotNew = reduce(dotOld)
    dotNew.write("outputNew.dot")
