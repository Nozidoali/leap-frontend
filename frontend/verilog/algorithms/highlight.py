import pygraphviz as pgv

highlightColors_extended = {
    "CYAN": {"fillcolor": "#B3E5FC", "fontcolor": "#0288D1"},  # Light cyan, Dark cyan
    "INDIGO": {
        "fillcolor": "#C5CAE9",
        "fontcolor": "#303F9F",
    },  # Light indigo, Dark indigo
    "VIOLET": {
        "fillcolor": "#D1C4E9",
        "fontcolor": "#512DA8",
    },  # Light violet, Dark violet
    "TEAL": {"fillcolor": "#B2DFDB", "fontcolor": "#00796B"},  # Light teal, Dark teal
    "GREY_BLUE": {
        "fillcolor": "#B0BEC5",
        "fontcolor": "#37474F",
    },  # Light grey-blue, Dark grey-blue
    "GREEN": {
        "fillcolor": "#C8E6C9",
        "fontcolor": "#388E3C",
    },  # Light green, Dark green
    "PURPLE": {
        "fillcolor": "#E1BEE7",
        "fontcolor": "#7B1FA2",
    },  # Light purple, Dark purple
    "ORANGE": {
        "fillcolor": "#FFE0B2",
        "fontcolor": "#FF6F00",
    },  # Light orange, Dark orange
}


def applyToFrame(graph: pgv.AGraph, variables: list, func: callable):
    # color the nodes reachable from the current node
    for node in graph.nodes():
        if node.attr["label"] in variables:
            _applyToSuccessorsRec(node, set(), func)
            _applyToPredecessorsRec(node, set(), func)


def _applyToSuccessorsRec(
    graph: pgv.AGraph, node: pgv.Node, visited: set, func: callable
):
    func(node)
    visited.add(node)
    for child in graph.successors(node):
        if child not in visited:
            _applyToSuccessorsRec(child, visited, func)


def _applyToPredecessorsRec(
    graph: pgv.AGraph, node: pgv.Node, visited: set, func: callable
):
    func(node)
    visited.add(node)
    for child in graph.predecessors(node):
        if child not in visited:
            _applyToPredecessorsRec(child, visited, func)


def highlightNode(node: pgv.Node, color: str = "CYAN"):
    node.attr["color"] = highlightColors_extended[color]["fontcolor"]
    node.attr["style"] = "filled"
    node.attr["fillcolor"] = highlightColors_extended[color]["fillcolor"]
    # text color
    node.attr["fontcolor"] = highlightColors_extended[color]["fontcolor"]
