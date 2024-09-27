## Assumptions:
# 1. The name of the "end" signal is known (default: "finish")
# 2. The name of the "reset" signal is known (default: "reset")

if __name__ == "__main__":
    from frontend import *
    import pygraphviz as pgv

    network: Netlist = readVerilog("examples/verilogs/external/legup.v")
    # network: Netlist = readVerilog("examples/verilogs/external/vitis.v")
    module = network.getModuleAt(0)
    # graph: pgv.AGraph = exportDOT(module)
    graph: pgv.AGraph = exportDOT(
        module, params={"skipConstants": False, "skipSignals": []}
    )

    ctrl_names = ["ap_done", "ap_idle", "ap_ready", "finish"]
    outputsNames = [
        port
        for port in module.getPortsByType(PortDirection.OUTPUT)
        if port not in ctrl_names
    ]

    outputDot = "toy"
    extractDataFlowControlFlow(module, graph, outputsNames)
    graph.write("{}.dot".format(outputDot))

    newModule = graphToBNGraph(module, graph, "cluster_control_flow")
    writeVerilog(newModule, "out.v")

    # CDFG = buildOriginalCDFG(graph, module)
    # CDFG.write("{}_CDFG.dot".format(outputDot))
