from ..modules import *
import pygraphviz as pgv


def _exportDOTRec(graph: pgv.AGraph, node: DFGNode) -> str:
    if node.isVariable():
        name = node.toString()
        label = name
        shape = "box"
    else:
        name = graph.number_of_nodes()
        label = node.name
        shape = "ellipse"

    graph.add_node(
        name,
        label=label,
        shape=shape,
    )
    for child in node.children:
        child_idx = _exportDOTRec(graph, child)
        graph.add_edge(child_idx, name)
    return name


def exportDOT(module: Module, params: dict = {}) -> pgv.AGraph:
    graph = pgv.AGraph(strict=False, directed=True)
    graph.graph_attr["splines"] = "ortho"
    graph.graph_attr["rankdir"] = "TB"  # Top-to-bottom layout

    # parse the params
    skipConstants = params.get("skipConstants", True)
    skipSignals = params.get("skipSignals", ["reset", "rst"])

    assignment: Assignment
    for i, assignment in enumerate(module.assignments):
        if (
            skipConstants
            and assignment.expression.isConstant()
            and assignment.condition is None
        ):
            continue

        id_lhs = _exportDOTRec(graph, assignment.target)
        if not assignment.expression.isConstant() or not skipConstants:
            id_rhs = _exportDOTRec(graph, assignment.expression)

            # add the edge from the rhs to the lhs
            graph.add_edge(id_rhs, id_lhs, xlabel=f"val{i}")

        # add the edge from the condition to the lhs
        if assignment.condition is not None:
            id_con = _exportDOTRec(graph, assignment.condition)
            graph.add_edge(
                id_con, id_lhs, style="dashed", color="red", xlabel=f"cond{i}"
            )

    graph.layout(prog="dot")

    # Remove reset node
    nodes_list = list(graph.nodes())
    for node in nodes_list:
        if node in skipSignals:
            graph.remove_node(node)

    return graph
