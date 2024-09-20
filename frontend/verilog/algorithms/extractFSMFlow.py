from ..modules import *
import re

def extractDataFlowNodes_rec(graph: pgv.AGraph, node: pgv.Node, visited: set):
    if node in visited:
        return
    visited.add(node)
    for edge in graph.in_edges(node):
        # do not traverse condition
        if( graph.get_edge(edge[0], edge[1]).attr["style"] != "dashed" ):
            extractDataFlowNodes_rec(graph, edge[0], visited)

def extractDataFlowControlFlowNodes( graph: pgv.AGraph , dataOutputs: list):

    dataNodes = set()
    controlNodes = []
    for out in dataOutputs:
        extractDataFlowNodes_rec(graph, out, dataNodes)
    for node in graph.nodes():
        if node not in dataNodes:
            controlNodes.append(node)
    return dataNodes, controlNodes

def extractDataFlowControlFlow( CDFG : pgv.AGraph, dataOutputs: list):
    dataNodes, controlNodes = extractDataFlowControlFlowNodes(CDFG, dataOutputs)
    dataGraph = CDFG.subgraph(dataNodes)
    controlGraph = CDFG.subgraph(controlNodes)
    return dataGraph, controlGraph