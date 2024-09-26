from ..modules import *
import pygraphviz as pgv


def addEdgeMap(map: dict, target: str, expression: str, cond: str , assignment: Assignment):
    map[(str(target), str(expression), str(cond) if cond != None else None)] = assignment
    return map

def foundDstCtrl(border_conn: list, cond: str):
    for src, dst in border_conn:
        if dst == cond or src == cond:
            return src, dst

    return None, None

def graphToBNGraph(module: Module, _graph: pgv.AGraph, subgraph: str=None) -> Module:
    outGraph = Module()
    if(subgraph == None):
        graph = _graph
    else:
        graph = _graph.get_subgraph(subgraph)

    mapping = module.node2assignment
    assert mapping != {}
    all_edges = graph.edges()
    all_nodes = graph.nodes()
    pis = [ module.getPort(port) for port in module.getPortsByType(PortDirection.INPUT) if port in all_nodes ]
    pos = [ module.getPort(port) for port in module.getPortsByType(PortDirection.OUTPUT) if port in all_nodes ]

    for pi in pis:
        outGraph.addPort(pi)
    
    for po in pos:
        outGraph.addPort(po)


    border_conn = []
    for src, dst in _graph.edges():
        if src in all_nodes and dst not in all_nodes:
            border_conn.append((src, dst))
        if src not in all_nodes and dst in all_nodes:
            border_conn.append((dst, src))

    
    input_cnt = 0
    output_cnt = 0

    for target, expression, cond in mapping.keys():
        assignment = mapping[(target, expression, cond)]
        expressionPresent = (expression, target) in all_edges
        conditionPresent = (cond, target) in all_edges
        print(cond, expressionPresent, conditionPresent, assignment.target.toString(), expression, target)
        if expressionPresent and conditionPresent:
            outGraph.addAssignment(assignment)
        elif expressionPresent:
            src, dst = foundDstCtrl(border_conn, expression)
            if src != None :
                newInputName = "newInput{}".format(input_cnt)
                input_cnt = input_cnt + 1
                newInput = DFGNode(newInputName)
                newInput.setRange(assignment.expression.range)
                assignment.setCondition(newInput)
                newInputPort = InputPort(newInput)
                outGraph.addPort(newInputPort)
                #border_conn.remove((expression, target))
            else:
                assignment.setCondition(None)
            outGraph.addAssignment(assignment)
        elif conditionPresent:
            if assignment.expression.isConstant():
                outGraph.addAssignment(assignment)
            else:
                assert False # this case is not considered yet
        elif expression not in all_nodes and target not in all_nodes:
            src, dst = foundDstCtrl(border_conn, cond)
            if src == None:
                continue
            border_conn.remove( (src, dst) )
            newOutputName = "newOutput{}".format(output_cnt)
            output_cnt = output_cnt + 1
            newOutput = DFGNode(newOutputName)
            newOutput.setRange(assignment.condition.range)
            assignment.setCondition(None)
            assignment.target = newOutput
            assignment.expression = cond
            newOutputPort = OutputPort(newOutput)
            outGraph.addPort(newOutputPort)

    print(border_conn)

    #assert len(border_conn) == 0 ## if it's false there are missing feature to consider other border connections

    return outGraph

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
            node2assignment = addEdgeMap(node2assignment, id_lhs, id_rhs, id_con, assignment)

    graph.layout(prog="dot")

    # Remove reset node
    nodes_list = list(graph.nodes())
    for node in nodes_list:
        if node in skipSignals:
            graph.remove_node(node)

    module.node2assignment = node2assignment

    return graph
