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

    ctrl_output_names = ["ap_done", "ap_idle", "ap_ready", "finish", "ap_start"]
    ctrl_input_names = [
        "start",
        "memory_controller_waitrequest",
        "clk",
        "clk2x",
        "clk1x_follower",
        "reset",
        "rst",
        "ap_rst",
        "ap_reset",
    ]
    outputsNames = [
        port
        for port in module.getPortsByDir(PortDirection.OUTPUT)
        if port not in ctrl_output_names
    ]

    inputsNames = [
        port
        for port in module.getPortsByDir(PortDirection.INPUT)
        if port not in ctrl_input_names
    ]

    outputDot = "toy"
    extractDataFlowControlFlow(module, graph, outputsNames, inputsNames)
    graph.write("{}.dot".format(outputDot))

    # newModule = graphToBNGraph(module, graph, "cluster_control_flow")
    # writeVerilog(newModule, "out.v")

    FSM = extractFSMGraph(module, graph)
    FSM.write("{}_FSM.dot".format(outputDot))

    CDFG = buildOriginalCDFG(graph, module, FSM, ["finish", "ap_done"])
    CDFG.write("{}_CDFG.dot".format(outputDot))
