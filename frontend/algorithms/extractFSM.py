from ..modules import *
from .highlight import *
import pygraphviz as pgv


def _extractDataFlowNodesRec(module:Module, graph: pgv.AGraph, node: pgv.Node, visited: set, revTraversal: bool):
    if node in visited:
        return
    visited.add(node)
    if revTraversal:
        edges = graph.in_edges(node)
    else:
        edges = graph.out_edges(node)
    for edge in edges:
        # do not traverse condition
        if isEdgeCond(edge[0], edge[1], graph, module) == False: 
            if revTraversal:
                nextNode = edge[0]
            else:
                nextNode = edge[1]
            _extractDataFlowNodesRec(module, graph, nextNode, visited, revTraversal)

def isExprCondition(expr: BNode):
    if expr.variable_name == "&&" or expr.variable_name == "||" or expr.variable_name == "!":
        return True
    if expr.variable_name == "==" or expr.variable_name == "!=":
        return True
    if expr.variable_name == "<" or expr.variable_name == "<=" or expr.variable_name == ">" or expr.variable_name == ">=":
        return True
    return False

def isEdgeCond(src: pgv.Node, dst: pgv.Node, graph: pgv.AGraph, module: Module):
    isCtrl = graph.get_edge(src, dst).attr["style"] == "dashed"
    if isCtrl:
        return True
    
    if module.isDefined(dst.get_name()):
        for target, expression, cond in module.node2assignment.keys():
            if expression == src.get_name() and target == dst.get_name():
                assign = module.node2assignment[(target, expression, cond)]
                expr = assign.expression
                if isExprCondition(expr):
                    return True
                break
    return False


def checkDataFlowNode_rec(module: Module, node: pgv.Node, origNode: pgv.Node , graph: pgv.AGraph, additionalNodes: set, existingNodes: set):
    successTrav = False
    for src, dst in graph.out_edges(node):
        if dst in existingNodes or dst in additionalNodes:
            continue
        if isEdgeCond(src, dst, graph, module):
            if src != origNode:
                additionalNodes.remove(src) # it's added by next function
                _extractDataFlowNodesRec(module, graph, src, additionalNodes, True)
            successTrav = True
            continue

        additionalNodes.add(dst)
        status = checkDataFlowNode_rec(module, dst, origNode, graph, additionalNodes, existingNodes)
        if not status:
            additionalNodes.remove(dst)
        else:
            successTrav = True
            if src != origNode:
                additionalNodes.remove(src) # it's added by next function
                _extractDataFlowNodesRec(module, graph, src, additionalNodes, True)

    if not successTrav:
        return False

    return True

def extractDataFlowControlFlowNodes(module: Module, graph: pgv.AGraph, dataOutputs: list, dataInputs: list):
    dataNodes = set()
    controlNodes = []
    for out in dataOutputs:
        _extractDataFlowNodesRec(module, graph, out, dataNodes, True)
    origNodes = dataNodes.copy()
    dataNodesNew = set()
    for inp in dataInputs:
        _extractDataFlowNodesRec(module, graph, inp, dataNodesNew, False)
    dataNodes.update(dataNodesNew)
    allAdditionalNodes = set()
    ## make sure that the condition is correctly captured
    for node in dataNodes:
        additionalNodes = set()
        additionalNodes.add(node)
        checkDataFlowNode_rec(module, node, node, graph, additionalNodes, dataNodes)
        if len(additionalNodes) > 1:
            allAdditionalNodes.update(additionalNodes)
    dataNodes.update(allAdditionalNodes)
    for node in graph.nodes():
        if node not in dataNodes:
            controlNodes.append(node)
    return dataNodes, controlNodes


def extractDataFlowControlFlow(module: Module, graph: pgv.AGraph, dataOutputs: list, dataInputs: list):
    dataNodes, controlNodes = extractDataFlowControlFlowNodes(module, graph, dataOutputs, dataInputs)
    dataGraph = graph.add_subgraph(
        dataNodes,
        name="cluster_data_flow",
        label="DATA_FLOW",
    )
    dataGraph.graph_attr["rank"] = "same"
    for node in dataGraph.nodes():
        highlightNode(node, "CYAN")

    controlGraph = graph.add_subgraph(
        controlNodes,
        name="cluster_control_flow",
        label="CONTROL_FLOW",
    )
    for node in controlGraph.nodes():
        highlightNode(node, "PURPLE")
    controlGraph.graph_attr["rank"] = "same"

    # we create a subgraph for the edges between data and control nodes
    toRemove, toAddRed, toAddBlue = [], [], []
    ioNames = []
    for edge in graph.edges():
        src = edge[0]
        dst = edge[1]
        if src in dataNodes and dst in controlNodes:
            toRemove.append(edge)
            ctrlName = f"ctrl_{len(ioNames)}"
            ioNames.append(ctrlName)
            toAddRed.append((src, ctrlName))
            toAddBlue.append((ctrlName, dst))
        elif src in controlNodes and dst in dataNodes:
            toRemove.append(edge)
            ctrlName = f"ctrl_{len(ioNames)}"
            ioNames.append(ctrlName)
            toAddBlue.append((src, ctrlName))
            toAddRed.append((ctrlName, dst))
        else:
            # set the color of the edge to black
            edge.attr["color"] = "black"
            edge.attr["style"] = "solid"
            continue
    ioNodes = []
    for ctrlName in ioNames:
        graph.add_node(ctrlName)
        node = graph.get_node(ctrlName)
        ioNodes.append(node)
        highlightNode(node, "GREEN")
    ioGraph = graph.add_subgraph(
        ioNodes,
        name="cluster_io",
        label="FSM I/O",
    )
    ioGraph.graph_attr["rank"] = "same"

    for edge in toRemove:
        graph.remove_edge(edge[0], edge[1])
    for edge in toAddRed:
        graph.add_edge(edge[0], edge[1], color="red", style="dashed")
    for edge in toAddBlue:
        graph.add_edge(edge[0], edge[1], color="blue", style="dashed")
    # Set the graph attributes
    graph.graph_attr["rankdir"] = "TB"  # Arrange top-to-bottom
    graph.graph_attr["overlap"] = "false"  # Prevent overlapping
    graph.graph_attr["ranksep"] = "1.0"  # Increase space between ranks (optional)

    graph.layout(prog="dot")

def findCondVar(node: BNode, op: str , var: str):
    if node.variable_name == op:
        if node.children[0].variable_name == var:
            return node
    for child in node.children:
        res = findCondVar(child, op, var)
        if res is not None:
            return res
    return None

def extractFSMGraph(module: Module, graph: pgv.AGraph):
    CFG = graph.get_subgraph("cluster_control_flow")
    FSM = pgv.AGraph(strict=False, directed=True)
    FSM.graph_attr["splines"] = "ortho"
    FSM.graph_attr["rankdir"] = "TB"  # Top-to-bottom layout

    states = module.getPortsByType(PortType.LOCALPARAM)
    states += module.getPortsByType(PortType.PARAMETER)

    statesVar = []
    for assign in module.assignments:
        if assign.expression.toString() in states:
            if assign.target.toString() not in statesVar:
                statesVar.append(assign.target.toString())
    if len(statesVar) == 0:
        raise Exception("No next state variable found")
    if len(statesVar) > 2:
        raise Exception("More than two states variable found")

    currStateVar = None
    nextStateVar = None
    for var in statesVar:
        statesTmp = states.copy()
        for assign in module.getAssignmentsOf(var):
            if assign.expression.toString() in statesTmp:
                statesTmp.remove(assign.expression.toString())
        if len(statesTmp) == 0:
            if nextStateVar is not None:
                raise Exception("More than one next state variable found")
            nextStateVar = var
        else:
            if currStateVar is not None:
                raise Exception("More than one current state variable found")
            currStateVar = var

    foundCurrStateAssign = False
    for assign in module.getAssignmentsOf(currStateVar):
        if assign.expression.toString() == nextStateVar:
            foundCurrStateAssign = True
            break
    assert foundCurrStateAssign, "The current and next state variables are not connected"

    startState = None
    for assign in module.getAssignmentsOf(currStateVar):
        if assign.expression.toString() in states:
            assert startState is None, "More than one reset state found"
            startState = assign.expression.toString()
    
    if startState is None:
        raise Exception("No reset state found")
    
    for state in states:
        FSM.add_node(state, shape="ellipse", color="green")

    for assign in module.getAssignmentsOf(nextStateVar):
        if assign.condition is None:
            continue
        stateDst = assign.expression.toString()
        if stateDst == currStateVar:
            continue
        condition = assign.condition
        condCurrState = findCondVar(condition, "==", currStateVar)
        condCurrStateExpr = condCurrState.children[1].variable_name
        assert condCurrStateExpr in states, "The condition is not a state variable"
        stateSrc = condCurrStateExpr
        FSM.add_edge(stateSrc, stateDst, color="red")

    return FSM

def isOpNode(node: pgv.Node):
    return node.attr["shape"] == "ellipse"


def isVarNode(node: pgv.Node):
    return node.attr["shape"] == "box"


def getArrivalState_rec(
    CFG: pgv.AGraph,
    node: pgv.Node,
    visited: set,
    module: Module,
    end_nodes: list,
    FSM: pgv.AGraph,
):
    if node in visited:
        return None
    visited.add(node)
    if node in FSM.nodes():
        return node
    if node.attr["label"] in end_nodes:
        return node
    for src, dst in CFG.out_edges(node):
        if isOpNode(dst):
            op_value = dst.attr["label"]
            if op_value == "~":
                continue
        dstNode = getArrivalState_rec(
            CFG, dst, visited, module, end_nodes, FSM
        )
        if dstNode is not None:
            return dstNode
    return None


# function to extract the arrival states of the data-controlled CFG
def getArrivalStates(
    graph: pgv.AGraph, controlPaths: list, module: Module, end_nodes: list, FSM: pgv.AGraph
):
    arrivalStates = []
    CFG = graph.get_subgraph("cluster_control_flow")
    for dataNode, ctrlNode in controlPaths:
        controlInputNode = graph.out_edges(ctrlNode)[0][1]
        dstState = getArrivalState_rec(
            CFG, controlInputNode, set(), module, end_nodes, FSM
        )
        assert dstState is not None
        arrivalStates.append((dataNode, dstState))
    return arrivalStates

# function to extract the departure states of the ctrl data CFG
def getDepartureStates(graph: pgv.AGraph, controlPaths: list, module: Module, FSM: pgv.AGraph):
    departureStates = []
    for ctrlNode, dataNode in controlPaths:
        assert len(graph.in_edges(ctrlNode)) == 1
        controlOutputNode = graph.in_edges(ctrlNode)[0][0]
        print(controlOutputNode.get_name(), module.getDependencies(controlOutputNode.get_name()))
    return departureStates


# function to build the original CDFG with the extracted data flow
def buildOriginalCDFG(graph: pgv.AGraph, module: Module, FSM: pgv.AGraph, end_nodes: list):
    CDFG = pgv.AGraph(strict=False, directed=True)
    CDFG.graph_attr["splines"] = "ortho"
    CDFG.graph_attr["rankdir"] = "TB"  # Top-to-bottom layout

    inCtrlOutDataWire = []
    outCtrlInDataWire = []

    # collect all the control paths that come from data flow nodes
    for srcNode, dstNode in graph.edges():
        srcIsDataNode = srcNode in graph.get_subgraph("cluster_data_flow").nodes()
        dstIsDataNode = dstNode in graph.get_subgraph("cluster_data_flow").nodes()
        if srcIsDataNode and dstIsDataNode:
            CDFG.add_edge(srcNode.get_name(), dstNode.get_name(), color="blue", style="dashed")
        elif srcIsDataNode:
            ## if the source node is a data node and the destination node is a control node
            ## this is a control path from data to control
            CDFG.add_node(srcNode.get_name())
            inCtrlOutDataWire.append((srcNode, dstNode))
        elif dstIsDataNode:
            CDFG.add_node(dstNode.get_name())
            outCtrlInDataWire.append((srcNode, dstNode))

    print(inCtrlOutDataWire, "AAAAAA")

    for node in CDFG.nodes():
        name = graph.get_node(node).attr["label"]
        CDFG.get_node(node).attr["label"] = name
        shape = graph.get_node(node).attr["shape"]
        CDFG.get_node(node).attr["shape"] = shape

    arrivalStates = getArrivalStates(graph, inCtrlOutDataWire, module, end_nodes, FSM)
    departureStates = {}
    #departureStates = getDepartureStates(graph, outCtrlInDataWire, module, FSM)
    for dataNode, arrivalState in arrivalStates:
        if arrivalState in end_nodes:
            CDFG.add_edge(dataNode.get_name(), arrivalState.get_name(), color="red", style="dashed")
        elif arrivalState in departureStates.keys():
            pass
            #CDFG.add_edge(dataNode, arrivalState, color="green", style="dashed")
        else:
            assert False, "Arrival state not found"

    return CDFG
