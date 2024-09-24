from ..modules import *
from .highlight import *
import pygraphviz as pgv


def extractARG(graph: pgv.AGraph):
    argGraph = graph.add_subgraph(
        name="cluster_arg", label="args", style="dashed", color="purple"
    )
    node: pgv.Node
    for node in graph.nodes():
        if node.attr["label"].startswith("arg"):
            argGraph.graph_attr["rankdir"] = "LR"
            argGraph.add_node(node)
            highlightNode(node, "PURPLE")
