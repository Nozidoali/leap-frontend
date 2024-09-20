## Assumptions:
# 1. The name of the "end" signal is known (default: "finish")
# 2. The name of the "reset" signal is known (default: "reset")

if __name__ == '__main__':
    from frontend import *

    
    parameters = {
        "extractFSM": False,
        "extractCIP": False,
        "extractARG": False,
        "extractREG": False,
    }

    network : Netlist = readVerilog("examples/tmp.v")
    module = network.getModule("toy")
    finishPort = "finish"
    outputsNames = [ port for port in  module.getPortsByType(PortDirection.OUTPUT) if port != finishPort]
    CDFG = module.getGraph()
    DFG, CFG = extractDataFlowControlFlow( CDFG , outputsNames)
    module.separateCDFG(DFG, CFG)
    #module.exportDOT(params=parameters)
    #module.exportDOT()
    module.writeDOT("toy.dot")
