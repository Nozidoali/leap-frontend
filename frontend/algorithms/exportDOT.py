from ..modules import *
import pygraphviz as pgv


def addEdgeMap(
    map: dict, target: str, expression: str, cond: str, assignment: Assignment
):
    map[(str(target), str(expression), str(cond) if cond != None else None)] = (
        assignment
    )
    return map


def foundCtrl_rec(graph: pgv.AGraph, src: str, dst: str):
    list_nodes = [src]
    visited = [src]
    while len(list_nodes) > 0:
        src = list_nodes.pop()
        for inV, outV in graph.out_edges(src):
            if outV == dst:
                return True
        for inV, outV in graph.out_edges(src):
            # check that the node is not a variable
            if outV not in visited and graph.get_node(outV).attr["shape"] != "box":
                list_nodes.append(outV)
                visited.append(outV)
    return False


def foundCtrl(graph: pgv.AGraph, border_conn: list, target: str, cond: str):
    found = False
    for src, dst in border_conn:
        if src == cond or dst == cond:
            found = True
    if not found:
        return None, None
    ctrlValue = None
    for src, dst in graph.out_edges(cond):
        if "ctrl_" in dst:
            if foundCtrl_rec(graph, dst, target):
                ctrlValue = dst
                break
    for src, dst in border_conn:
        if (src == cond and dst == ctrlValue) or (src == ctrlValue and dst == cond):
            return src, dst

    return None, None


def graphToBNGraph(module: Module, _graph: pgv.AGraph, subgraph: str = None) -> Module:
    outGraph = Module()
    if subgraph == None:
        graph = _graph
    else:
        graph = _graph.get_subgraph(subgraph)

    mapping = module.node2assignment
    assert mapping != {}
    all_edges = graph.edges()
    all_nodes = graph.nodes()
    pis = [
        module.getPort(port)
        for port in module.getPortsByDir(PortDirection.INPUT)
        if port in all_nodes
    ]
    pos = [
        module.getPort(port)
        for port in module.getPortsByDir(PortDirection.OUTPUT)
        if port in all_nodes
    ]
    parameters = [
        module.getPort(port)
        for port in module.getPortsByType(PortType.PARAMETER)
        if port in all_nodes
    ]
    localparams = [
        module.getPort(port)
        for port in module.getPortsByType(PortType.LOCALPARAM)
        if port in all_nodes
    ]

    for pi in pis:
        outGraph.addPort(pi)
    for po in pos:
        outGraph.addPort(po)
    for param in parameters:
        outGraph.addPort(param)
    for localparam in localparams:
        outGraph.addPort(localparam)

    border_conn = []
    for src, dst in _graph.edges():
        if src in all_nodes and dst not in all_nodes:
            assert "ctrl_" in dst
            border_conn.append((src, dst))
        if src not in all_nodes and dst in all_nodes:
            border_conn.append((dst, src))
            assert "ctrl_" in src

    for target, expression, cond in mapping.keys():
        assignment = mapping[(target, expression, cond)]
        ## skipping initial assignements values unless it's a parameter
        modulePort = module.getPort(assignment.target.toString())
        if modulePort != None and (
            modulePort.getType() == PortType.LOCALPARAM
            or modulePort.getType() == PortType.PARAMETER
        ):
            isParameter = True
        else:
            isParameter = False
        if cond == None and assignment.expression.isConstant() and not isParameter:
            continue
        srcCtrl, dstCtrl = foundCtrl(_graph, border_conn, target, cond)
        if not target in all_nodes and (dstCtrl == None or not "ctrl_" in dstCtrl):
            continue
        if srcCtrl == None:
            outGraph.addAssignment(assignment)
        elif "ctrl_" in srcCtrl:
            newInputName = srcCtrl
            newInput = BNode(newInputName)
            newInput.setRange(assignment.expression.range)
            assignment.condition = newInput
            newInputPort = InputPort(newInput)
            outGraph.addPort(newInputPort)
            outGraph.addAssignment(assignment)
            border_conn.remove((srcCtrl, dstCtrl))
        elif "ctrl_" in dstCtrl:
            newOutputName = dstCtrl
            newOutput = BNode(newOutputName)
            newOutput.setRange(assignment.condition.range)
            assignment.target = newOutput
            assignment.expression = assignment.condition
            assignment.condition = None
            newOutputPort = OutputPort(newOutput)
            outGraph.addPort(newOutputPort)
            outGraph.addAssignment(assignment)
            border_conn.remove((srcCtrl, dstCtrl))

    # assert len(border_conn) == 0 ## if it's false there are missing feature to consider other border connections

    return outGraph


def _exportDOTRec(graph: pgv.AGraph, node: BNode) -> str:
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

    # node-to-assignment map
    node2assignment = {}

    # parse the params
    skipConstants = params.get("skipConstants", True)
    skipSignals = params.get("skipSignals", ["reset", "rst", "ap_rst", "ap_reset"])

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
        else:
            id_con = None

        if not skipConstants and skipSignals == []:
            node2assignment = addEdgeMap(
                node2assignment, id_lhs, id_rhs, id_con, assignment
            )

    graph.layout(prog="dot")

    # Remove reset node
    nodes_list = list(graph.nodes())
    for node in nodes_list:
        if node in skipSignals:
            graph.remove_node(node)

    module.node2assignment = node2assignment

    return graph
