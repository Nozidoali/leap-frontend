import pygraphviz as pgv
import re

from ..modules import *
from .highlight import *

def extractCIP(graph: pgv.AGraph):
    CIPpairs = []
    for node in graph.nodes():
        # e.g. main_0_b_address_a and main_0_b_out_a
        if re.match(r".*address.*", node.attr["label"]):
            try:
                outNode = graph.get_node(node.attr["label"].replace("address", "out"))
            except KeyError:
                outNode = None
            try:
                inNode = graph.get_node(node.attr["label"].replace("address", "in"))
            except KeyError:
                inNode = None
            CIPpairs.append((node, outNode, inNode))

    for i, (addressNode, outNode, inNode) in enumerate(CIPpairs):
        cipGraph = graph.add_subgraph(
            name=f"cluster_cip{i}", label="CIP", style="dashed", color="green"
        )
        cipGraph.graph_attr["rankdir"] = "TB"

        for node in [addressNode, outNode, inNode]:
            if node is not None:
                cipGraph.add_node(node)
                highlightNode(node, "GREEN")
