from ..modules import *
from .highlight import *
import pygraphviz as pgv


def extractREG(graph: pgv.AGraph):
    stages = {}
    for node in graph.nodes():
        # match the state number, the name should be ..._reg_stage<num>
        try:
            stage = int(re.search(r"_reg_stage(\d+)", node.attr["label"]).group(1))
            if stage not in stages:
                stages[stage] = []
            stages[stage].append(node)
        except AttributeError:
            continue

    for stage, nodes in stages.items():
        regGraph = graph.add_subgraph(
            name=f"cluster_reg{stage}",
            label=f"pipeline stage \#{stage}",
            style="dashed",
            color="orange",
        )
        regGraph.graph_attr["rankdir"] = "TB"
        for node in nodes:
            regGraph.add_node(node)
            highlightNode(node, "ORANGE")
