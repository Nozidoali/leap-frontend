from typing import List, Dict

from .cdfg.cdfg import *


def technologyMapping(cdfgOld: CDFGraph) -> CDFGraph:
    cdfgNew = CDFGraph()

    # old node name to new node name mapping
    oldToNew: Dict[str, str] = {}

    # Iterate over all nodes in the graph and recreate DFGNodes
    for nodeOld in cdfgOld.nodes():
        nodeNew = cdfgOld.toBNode(nodeOld)
        newNodeId = cdfgNew.add_node(nodeNew)

        oldToNew[nodeOld] = newNodeId

        # Get predecessors
        for child in cdfgOld.predecessors(nodeOld):
            # Get the edge type
            idx = cdfgOld.get_edge(child, nodeOld).attr["eIndex"]
            edgeType = cdfgOld.get_edge(child, nodeOld).attr["eType"]

            # Add the edge to the new graph
            childId = (
                cdfgNew.add_node(cdfgOld.toBNode(child))
                if child not in oldToNew
                else oldToNew[child]
            )
            cdfgNew.addEdge(childId, newNodeId, idx, edgeType)

            # Add the child to the new node
            nodeNew.children.append(cdfgOld.toBNode(child))

    return cdfgNew
