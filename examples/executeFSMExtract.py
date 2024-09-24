## Assumptions:
# 1. The name of the "end" signal is known (default: "finish")
# 2. The name of the "reset" signal is known (default: "reset")

if __name__ == "__main__":
    from frontend import *
    import pygraphviz as pgv

    network: Netlist = readVerilog("examples/verilogs/external/legup2.v")
    module = network.getModuleAt(0)
    graph: pgv.AGraph = exportDOT(module)

    outputsNames = [
        port for port in module.getPortsByType(PortDirection.OUTPUT) if port != "finish"
    ]

    extractDataFlowControlFlow(graph, outputsNames)
    graph.write("tmp.dot")
