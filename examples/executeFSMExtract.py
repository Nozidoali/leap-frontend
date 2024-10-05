## Assumptions:
# 1. The name of the "end" signal is known (default: "finish")
# 2. The name of the "reset" signal is known (default: "reset")

if __name__ == "__main__":
    from frontend import *
    import pygraphviz as pgv

    outputDot = "gaussian"
    network: Netlist = readVerilog("examples/verilogs/external/legup/{}.v".format(outputDot))
    # network: Netlist = readVerilog("examples/verilogs/external/vitis.v")
    module = network.getModuleAt(0)
    # graph: pgv.AGraph = exportDOT(module)
    graph: pgv.AGraph = exportDOT(
        module, params={"skipConstants": False, "skipSignals": []}
    )

    mult_connect(graph)

    ctrl_output_names = ["ap_done", "ap_idle", "ap_ready", "finish", "ap_start"]
    ctrl_input_names = ["start", "memory_controller_waitrequest", "clk", "clk2x", "clk1x_follower", "reset", "rst", "ap_rst", "ap_reset"]
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

    extractDataFlowControlFlow(module, graph, outputsNames, inputsNames)
    graph.write("{}.dot".format(outputDot))

    #newModule = graphToBNGraph(module, graph, "cluster_control_flow")
    #writeVerilog(newModule, "out.v")

    FSM = extractFSMGraph(module, graph)
    FSM.write("{}_FSM.dot".format(outputDot))

    # keywords for memory ports
    
    memory_keywords = {}
    memory_keywords["regex_memory"] = [r"main_0_(?P<memory_name>[a-zA-Z0-9_]+)_address_(?P<memory_id>[a-z])"]
    memory_keywords["outAddress"] = ["main_0_MEMORY_NAME_address_MEMORY_ID"]
    #memory_keywords["inAddress"] = ["arg_MEMORY_NAME"]
    memory_keywords["outMemory"] = ["main_0_MEMORY_NAME_out_MEMORY_ID"]
    memory_keywords["inMemory"] = ["main_0_MEMORY_NAME_in_MEMORY_ID"]
    memory_keywords["writeEnable"] = ["main_0_MEMORY_NAME_write_enable_MEMORY_ID"]
    memory_keywords["enable"] = ["main_0_MEMORY_NAME_enable_MEMORY_ID"]

    CDFG = buildOriginalCDFG(graph, module, FSM, ["finish", "ap_done"], memory_keywords)
    CDFG.write("{}_CDFG.dot".format(outputDot))
