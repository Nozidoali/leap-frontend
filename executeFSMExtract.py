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
    DFG, CFG = extractDataFlowControlFlow( module.getGraph(), outputsNames)
    module.separateCDFG(DFG, CFG)
    #module.exportDOT(params=parameters)
    #module.exportDOT()
    module.writeDOT("toy.dot")
