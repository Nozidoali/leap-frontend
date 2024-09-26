from ..modules import *
from .highlight import *
import pygraphviz as pgv

def replaceCond(module: Module, srcCond: str, dstCond: str, newCond: str):
    mapping = module.node2assignment
    assert mapping is not {}
    keys = list(mapping.keys()).copy()
    for target, expression, cond in keys:
        if cond == srcCond and target == dstCond:
            assignment = mapping[(target, expression, cond)]
            del mapping[(target, expression, cond)]
            mapping[(target, expression, newCond)] = assignment
    module.node2assignment = mapping


def _extractDataFlowNodesRec(graph: pgv.AGraph, node: pgv.Node, visited: set):
    if node in visited:
        return
    visited.add(node)
    for edge in graph.in_edges(node):
        # do not traverse condition
        if graph.get_edge(edge[0], edge[1]).attr["style"] != "dashed":
            _extractDataFlowNodesRec(graph, edge[0], visited)


def extractDataFlowControlFlowNodes(graph: pgv.AGraph, dataOutputs: list):
    dataNodes = set()
    controlNodes = []
    for out in dataOutputs:
        _extractDataFlowNodesRec(graph, out, dataNodes)
    for node in graph.nodes():
        if node not in dataNodes:
            controlNodes.append(node)
    return dataNodes, controlNodes


def extractDataFlowControlFlow(module: Module, graph: pgv.AGraph, dataOutputs: list):
    dataNodes, controlNodes = extractDataFlowControlFlowNodes(graph, dataOutputs)
    dataGraph = graph.add_subgraph(
        dataNodes,
        name="cluster_data_flow",
        label="DATA_FLOW",
    )
    dataGraph.graph_attr["rank"] = "same"
    for node in dataGraph.nodes():
        highlightNode(node, "CYAN")

    controlGraph = graph.add_subgraph(
        controlNodes,
        name="cluster_control_flow",
        label="CONTROL_FLOW",
    )
    for node in controlGraph.nodes():
        highlightNode(node, "PURPLE")
    controlGraph.graph_attr["rank"] = "same"

    # we create a subgraph for the edges between data and control nodes
    toRemove, toAddRed, toAddBlue = [], [], []
    ioNames = []
    for edge in graph.edges():
        src = edge[0]
        dst = edge[1]
        if src in dataNodes and dst in controlNodes:
            toRemove.append(edge)
            ctrlName = f"ctrl_{len(ioNames)}"
            ioNames.append(ctrlName)
            toAddRed.append((src, ctrlName))
            toAddBlue.append((ctrlName, dst))
            replaceCond(module, src, dst, ctrlName)            
        elif src in controlNodes and dst in dataNodes:
            toRemove.append(edge)
            ctrlName = f"ctrl_{len(ioNames)}"
            ioNames.append(ctrlName)
            toAddBlue.append((src, ctrlName))
            toAddRed.append((ctrlName, dst))
            replaceCond(module, src, dst, ctrlName)
        else:
            # set the color of the edge to black
            edge.attr["color"] = "black"
            edge.attr["style"] = "solid"
            continue
    ioNodes = []
    for ctrlName in ioNames:
        graph.add_node(ctrlName)
        node = graph.get_node(ctrlName)
        ioNodes.append(node)
        highlightNode(node, "GREEN")
    ioGraph = graph.add_subgraph(
        ioNodes,
        name="cluster_io",
        label="FSM I/O",
    )
    ioGraph.graph_attr["rank"] = "same"

    for edge in toRemove:
        graph.remove_edge(edge[0], edge[1])
    for edge in toAddRed:
        graph.add_edge(edge[0], edge[1], color="red", style="dashed")
    for edge in toAddBlue:
        graph.add_edge(edge[0], edge[1], color="blue", style="dashed")
    # Set the graph attributes
    graph.graph_attr["rankdir"] = "TB"  # Arrange top-to-bottom
    graph.graph_attr["overlap"] = "false"  # Prevent overlapping
    graph.graph_attr["ranksep"] = "1.0"  # Increase space between ranks (optional)

    graph.layout(prog="dot")


def isOpNode(node: pgv.Node):
    return node.attr["shape"] == "ellipse"

def isVarNode(node: pgv.Node):
    return node.attr["shape"] == "box"

def getCondAssignment(module: Module, node: pgv.Node, cond: str):
    print(node)
    for assignment in module.getAssignmentsOf(node.get_name()):
        print(cond, assignment.condition.toString())
        if assignment.condition is not None and assignment.condition == cond:
            return assignment.expression
    return None

def isStateNode(module: Module, node: pgv.Node):
    variable_type = module.getVariableType(node.get_name())
    return variable_type == PortType.LOCALPARAM

def getArrivalState_rec(CDFG: pgv.AGraph, node: pgv.Node, visited: set, reachedStates : set, module: Module, end_node: str):
    if node in visited:
        return None
    print(node)
    visited.add(node)
    if node.attr["label"] == end_node:
        reachedStates.add(node)
        return None
    for src, dst in CDFG.out_edges(node):
        print(src, dst.attr["label"])
        if isOpNode(dst):
            op_value = dst.attr["label"]
            if op_value == "~":
                continue
        elif isVarNode(dst):
            var_name = dst.attr["label"]
            isCond = "cond" in CDFG.get_edge(src, dst).attr["xlabel"] 
            if var_name == end_node:
                reachedStates.add(dst)
                return None
            if isCond:
                assignedValue = getCondAssignment(module, dst, var_name)
                print(var_name)
                assert assignedValue is not None
                if isStateNode(assignedValue):
                    reachedStates.add(dst)
                    continue
        dstNode = getArrivalState_rec(CDFG, dst, visited, reachedStates, module, end_node)
    return None


# function to extract the arrival states of the data-controlled CFG
def getArrivalStates(graph: pgv.AGraph, controlPaths: list, module: Module, end_node: str):
    arrivalStates = []
    CFG = graph.get_subgraph("cluster_control_flow")
    for dataNode, ctrlNode in controlPaths:
        reachedStates = set()
        dstState = getArrivalState_rec(graph, ctrlNode, set(), reachedStates, module, end_node)
        assert dstState is not None
        arrivalStates.append((dataNode, dstState))
    return arrivalStates

# function to build the original CDFG with the extracted data flow
def buildOriginalCDFG(graph: pgv.AGraph, module: Module , end_node: str = "finish"):
    CDFG = pgv.AGraph(strict=False, directed=True)
    CDFG.graph_attr["splines"] = "ortho"
    CDFG.graph_attr["rankdir"] = "TB"  # Top-to-bottom layout

    for srcDataNode, dstDataNode in graph.get_subgraph("cluster_data_flow").edges():
        CDFG.add_edge(srcDataNode, dstDataNode, color="blue", style="dashed")

    # collect all the control paths that come from data flow nodes
    controlPaths = []
    for srcNode, dstNode in graph.edges():
        srcIsDataNode = srcNode in graph.get_subgraph("cluster_data_flow").nodes()
        dstIsDataNode = dstNode in graph.get_subgraph("cluster_data_flow").nodes()
        if srcIsDataNode and dstIsDataNode:
            CDFG.add_edge(srcNode, dstNode, color="blue", style="dashed")
        elif srcIsDataNode:
            ## if the source node is a data node and the destination node is a control node
            ## this is a control path from data to control
            CDFG.add_node(srcNode)
            controlPaths.append((srcNode, dstNode))
        elif dstIsDataNode:
            CDFG.add_node(dstNode)
    
    arrivalStates = getArrivalStates(graph, controlPaths, module, end_node)

    return CDFG

