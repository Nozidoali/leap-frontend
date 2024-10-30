## Assumptions:
# 1. The name of the "end" signal is known (default: "finish")
# 2. The name of the "reset" signal is known (default: "reset")

if __name__ == "__main__":
    from frontend import *
    import pygraphviz as pgv
    import os

    outputDot = "gaussian"
    external = "legup"
    results_folder = "results/{0}/{1}".format(external, outputDot)
    network: Netlist = readVerilog("examples/verilogs/external/{}/{}.v".format(external, outputDot))
    # network: Netlist = readVerilog("examples/verilogs/external/vitis.v")
    module = network.getModuleAt(0)
    # graph: pgv.AGraph = exportDOT(module)
    print("Started export dot")
    graph: pgv.AGraph = exportDOT(
        module, params={"skipConstants": False, "skipSignals": []}
    )
    print("Finished export dot")


    mult_connect(graph)

    ctrl_output_names = ["ap_done", "ap_idle", "ap_ready", "finish", "ap_start"]
    ctrl_input_names = ["start", "memory_controller_waitrequest", "clk", "clk2x", "clk1x_follower", "reset", "rst", "ap_rst", "ap_reset", "ap_start"]
    outputsNames = [
        port
        for port in module.getPortsByDir(PortDirection.OUTPUT)
        if port not in ctrl_output_names and port in graph.nodes()
    ]

    inputsNames = [
        port
        for port in module.getPortsByDir(PortDirection.INPUT)
        if port not in ctrl_input_names and port in graph.nodes()
    ]

    print("Extracting Data Flow Control Flow")

    extractDataFlowControlFlow(module, graph, outputsNames, inputsNames)
    graph.write("{0}/{1}.dot".format(results_folder , outputDot))

    #newModule = graphToBNGraph(module, graph, "cluster_control_flow")
    #writeVerilog(newModule, "out.v")

    print("Extracting FSM")

    resetSignals = ["reset", "rst", "ap_rst", "ap_reset"]

    FSM = extractFSMGraph(module, graph, resetSignals)
    FSM.write("{0}/{1}_FSM.dot".format(results_folder, outputDot))
    printFSMGraph(FSM, f"{results_folder}/{outputDot}_FSM.txt")


    # keywords for memory ports
    
    memory_keywords = {}
    memory_keywords["regex_memory"] = [r"main_0_(?P<memory_name>[a-zA-Z0-9_]+)_address_(?P<memory_id>[a-z])", r"(?P<memory_name>[a-zA-Z0-9_]+)_address(?P<memory_id>[0-9]+)"]
    memory_keywords["outAddress"] = ["main_0_MEMORY_NAME_address_MEMORY_ID", "MEMORY_NAME_addressMEMORY_ID"]
    #memory_keywords["inAddress"] = ["arg_MEMORY_NAME"]
    memory_keywords["outMemory"] = ["main_0_MEMORY_NAME_out_MEMORY_ID", "MEMORY_NAME_qMEMORY_ID"]
    memory_keywords["inMemory"] = ["main_0_MEMORY_NAME_in_MEMORY_ID", "MEMORY_NAME_dMEMORY_ID"]
    memory_keywords["writeEnable"] = ["main_0_MEMORY_NAME_write_enable_MEMORY_ID", "MEMORY_NAME_weMEMORY_ID"]
    memory_keywords["enable"] = ["main_0_MEMORY_NAME_enable_MEMORY_ID", "MEMORY_NAME_ceMEMORY_ID"]

    print("Building CDFG")

    CDFG, states2nodes = buildOriginalCDFG(graph, module, FSM, ["finish", "ap_done"], memory_keywords)
    
    #for state in states2nodes:
    #    print(state, states2nodes[state])
    #    print()

    CFG = extractCFGGraph(module, FSM)
    CFG.write("{0}/{1}_CFG.dot".format(results_folder, outputDot))
    CDFG = assignBBs2nodes(CDFG, states2nodes, CFG, FSM)
    CDFG.write("{0}/{1}_CDFG.dot".format(results_folder, outputDot))
    printCDFGBB(CDFG, CFG, f"{results_folder}/{outputDot}_CDFG_BB.dot")
    os.system("mv FSM_merged.dot {0}/{1}_FSM_merged.dot".format(results_folder, outputDot))
    os.system("mv FSM_* {0}".format(results_folder))
    os.system("mv phi_states.txt {0}".format(results_folder))

    print("Generating Verilog")

    jsonFile = "{0}/{1}.json".format(results_folder, outputDot)
    verilogFile = "{0}/{1}_CDFG.v".format(results_folder, outputDot)
    CDFGToVerilog(CDFG, FSM, module, verilogFile, jsonFile, memory_keywords, states2nodes)