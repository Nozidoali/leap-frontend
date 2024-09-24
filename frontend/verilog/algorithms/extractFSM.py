from ..modules import *
from .highlight import *
import pygraphviz as pgv


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


def extractDataFlowControlFlow(graph: pgv.AGraph, dataOutputs: list):
    dataNodes, _ = extractDataFlowControlFlowNodes(graph, dataOutputs)
    dataGraph = graph.subgraph(dataNodes)
    fsmGraph = graph.add_subgraph(
        dataGraph,
        name="cluster_data_flow",
        label="DATA_FLOW",
        style="dashed",
        color="blue",
    )
    fsmGraph.graph_attr["rankdir"] = "LR"  # Left-to-right layout

    for node in dataGraph.nodes():
        highlightNode(node, "CYAN")
