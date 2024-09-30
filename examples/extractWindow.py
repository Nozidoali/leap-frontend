from frontend import *

if __name__ == "__main__":
    netlist: Netlist = readVerilog("examples/verilogs/external/legup.v")
    dotOld = moduleToGraph(netlist.getModuleAt(0))
    dotOld = reduce(dotOld)
    dotOld.write("output.dot")
    elaborateConditionsAt(dotOld, "main_0_c_address_a")
    dotNew = extractWindow(dotOld, "main_0_c_address_a", ["loop_1_state_enable_0"])
    dotNew.write("outputNew.dot")
    moduleNew = graphToModule(dotNew)
    writeVerilog(moduleNew, "outputNew.v")
