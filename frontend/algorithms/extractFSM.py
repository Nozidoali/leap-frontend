from ..modules import *
from .highlight import *
import pygraphviz as pgv
from collections import deque
import re
import networkx as nx
import json
import sys

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
    if expr.variable_name == "==" or expr.variable_name == "!=" or expr.variable_name == "?:":
        return True
    if expr.variable_name == "<" or expr.variable_name == "<=" or expr.variable_name == ">" or expr.variable_name == ">=":
        return True
    return False

# find the subtree of the expression where var is a child
def getNodesExpr(expr: BNode, var: str):
    if len(expr.children) == 0:
        return None
    if expr.children[0].variable_name == var or expr.children[1].variable_name == var:
        return expr
    for child in expr.children:
        res = getNodesExpr(child, var)
        if res is not None:
            return res
    return None

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
    for  target, expression, condition  in module.node2assignment.keys():
        if target == dst.get_name() and condition == src.get_name():
            return True

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

    #graph.layout(prog="dot")

def findCondVar(node: BNode, op: str , var: str):
    if node.variable_name == op:
        if node.children[0].variable_name == var:
            return node
    for child in node.children:
        res = findCondVar(child, op, var)
        if res is not None:
            return res
    return None

# function to set top state in the FSM graph
def setFSMTopState(FSM: pgv.AGraph, module: Module, currStateVar: str, resetSignals: list):

    resetSignal = None
    for signal in resetSignals:
        if signal in module.getPorts():
            resetSignal = signal
            break
    assert resetSignal is not None, "Reset signal not found"
    startState = None
    for assign in module.getAssignmentsOf(currStateVar):
        if assign.condition.isVariable() and assign.condition.toString() == resetSignal:
            startState = assign.expression.toString()
            break
        elif assign.condition.isOperation() and assign.condition.variable_name == "==":
            if assign.condition.children[0].toString() == resetSignal and (assign.condition.children[1].toString() == "1'b1" or assign.condition.children[1].toString() == "1"):
                startState = assign.expression.toString()
                break
    assert startState is not None, "Start state not found"
    assert startState in FSM.nodes(), "Start state not found in FSM"
    topNode = FSM.get_node(startState)
    topNode.attr["comment"] = "Start"
    return FSM

def extractFSMGraph(module: Module, graph: pgv.AGraph, resetSignals: list):
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
        FSM.get_node(state).attr["info"] = "Curr_state: " + currStateVar + "|||Next_state: " + nextStateVar

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

    setFSMTopState(FSM, module, currStateVar ,resetSignals)

    return FSM

def getCurrStateVar(FSM: pgv.AGraph):
    for node in FSM.nodes():
        if "Curr_state" in FSM.get_node(node).attr["info"]:
            curr_state = FSM.get_node(node).attr["info"].split("|||")[0].split(":")[1].strip()
            return curr_state
    return None

def getNextStateVar(FSM: pgv.AGraph):
    for node in FSM.nodes():
        if "Next_state" in FSM.get_node(node).attr["info"]:
            next_state = FSM.get_node(node).attr["info"].split("|||")[1].split(":")[1].strip()
            return next_state
    return None

def isOpNode(node: pgv.Node):
    return node.attr["shape"] == "ellipse"


def isVarNode(node: pgv.Node):
    return node.attr["shape"] == "box"


def getAssignStatement(module: Module, target: str, expression: str, condition: str):
    targetIsNone = target is None
    expressionIsNone = expression is None
    conditionIsNone = condition is None
    assert not (targetIsNone and expressionIsNone) or not (targetIsNone and conditionIsNone), "Invalid arguments"
    for tmpTarget, tmpExpression, tmpCondition in module.node2assignment.keys():
        if expressionIsNone and tmpTarget == target and tmpCondition == condition:
            return module.node2assignment[(tmpTarget, tmpExpression, tmpCondition)]
        if targetIsNone and tmpExpression == expression and tmpCondition == condition:
            return module.node2assignment[(tmpTarget, tmpExpression, tmpCondition)]
    return None

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
    if node.attr["label"] in end_nodes:
        return node
    for src, dst in CFG.out_edges(node):
        if isOpNode(dst):
            op_value = dst.attr["label"]
            if op_value == "~":
                continue
        elif isVarNode(dst):
            if( isEdgeCond(src, dst, CFG, module) ):
                assign = getAssignStatement(module, dst, None, src)
                assert assign is not None, "Assignment statement not found"
                if assign.expression.isConstant():
                    value = assign.expression.toString()
                    if value == "1'b0" or value == "0" or value == "1'd0":
                        continue
                else:
                    expression = assign.expression.toString()
                    if expression in FSM.nodes():
                        return expression

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

def getDepartureStates_rec(
    CFG: pgv.AGraph,
    node: pgv.Node,
    visited: set,
    module: Module,
    nodes2reach: list,
    terminateTravNodes: list,
):
    if node in visited:
        return None
    if node in terminateTravNodes:
        return None
    if node in nodes2reach:
        nodes2reach.remove(node)
        return None
    visited.add(node)
    for src, dst in CFG.out_edges(node):
        if isOpNode(dst):
            op_value = dst.attr["label"]
            if op_value == "~":
                continue
        elif isVarNode(dst):
            if( isEdgeCond(src, dst, CFG, module) ):
                assign = getAssignStatement(module, dst, None, src)
                assert assign is not None, "Assignment statement not found"
                if assign.expression.isConstant():
                    value = assign.expression.toString()
                    if value == "1'b0" or value == "0" or value == "1'd0":
                        continue
                else:
                    target = assign.target.toString()
                    if target in nodes2reach:
                        nodes2reach.remove(target)
                        continue

        if dst in terminateTravNodes:
            continue
        dstNode = getDepartureStates_rec(
            CFG, dst, visited, module, nodes2reach, terminateTravNodes, 
        )
        if dstNode is not None:
            return dstNode
    return None

def isPatternPresent(node: BNode, lhs: str, rhs: str, op: str):
    if node.isOperation() and node.variable_name == op:
        if node.children[1].variable_name == rhs and node.children[0].variable_name == lhs:
            return True
    for child in node.children:
        if isPatternPresent(child, lhs, rhs, op):
            return True
    return False

def getAssignToNode(module: Module, assign: Assignment):
    for target, expression, condition in module.node2assignment.keys():
        if assign == module.node2assignment[(target, expression, condition)]:
            return target, expression, condition

def findPredecessor_DFS(graph: pgv.AGraph, node: pgv.Node, target: list, visited: set, path: list):
    
    path.append(node)
    if node in visited:
        return None
    visited.add(node)
    if node in target:
        return path
    for src, dst in graph.in_edges(node):
        if isOpNode(src):
            op_value = src.attr["label"]
            if op_value == "~":
                continue
        if src in ["reset", "rst", "ap_rst", "ap_reset"]:
            continue
        res = findPredecessor_DFS(graph, src, target, visited, path)
        if res is not None:
            return res
        path.pop()
    return None

def findPredecessor_BFS(module: Module, graph: pgv.AGraph, node: pgv.Node, target: list, visited: set):
    if module.isDefined(node) and module.getPort(node).getType() == PortType.REG:
        assignment = module.getAssignmentsOf(node)[0]
        event = assignment.event.toString()
        if "clk" in event or "clock" in event:
            numRegs = 1
        else:
            numRegs = 0
    else:
        numRegs = 0
    queue = deque([(node, [node], numRegs)])
    visited.add(node)

    while queue:
        current_node, current_path, numRegs = queue.popleft()
        if current_node in target:
            if module.isDefined(current_node) and module.getPort(current_node).getType() == PortType.REG:
                event = module.getAssignmentsOf(current_node)[0].event.toString()
                if "clk" in event or "clock" in event:
                    numRegs -= 1 # remove the register count for the src node
            return current_path, numRegs

        for src, dst in graph.in_edges(current_node):
            if isOpNode(src):
                op_value = src.attr["label"]
                if op_value == "~":
                    continue
            if src in ["reset", "rst", "ap_rst", "ap_reset"]:
                continue
            if src not in visited:
                visited.add(src)
                if module.isDefined(src) and module.getPort(src).getType() == PortType.REG:
                    event = module.getAssignmentsOf(src)[0].event.toString()
                    if "clk" in event or "clock" in event:
                        numRegs += 1
                queue.append((src, current_path + [src], numRegs))

    return None

# function to return if the control path is a pipeline
def checkPipeline(candidateCouts: list, currStateVar: str, nextStateVar: str, graph: pgv.AGraph, module: Module):
    pipelineGraph = None
    for ctrl in candidateCouts:
        targets = [currStateVar, nextStateVar]
        targets.extend(candidateCouts)
        targets.remove(ctrl)
        path, numRegs = findPredecessor_BFS(module, graph, ctrl, targets, set())
        #path = findPredecessor_DFS(graph, ctrl, targets, set(), [])
        assert path is not None, "Path not found"
        srcPipelineState = None
        for node in path:
            if node != ctrl and node in candidateCouts:
                srcPipelineState = node 
                dstPipelineState = ctrl
                break
        if srcPipelineState is not None:
            if pipelineGraph is None:
                pipelineGraph = pgv.AGraph(strict=False, directed=True)
                pipelineGraph.graph_attr["splines"] = "ortho"
                pipelineGraph.graph_attr["rankdir"] = "TB"
            pipelineGraph.add_edge(srcPipelineState, dstPipelineState, color="red", info="NumRegs=" + str(numRegs))

    return pipelineGraph

def findTopNode(graph: pgv.AGraph):
    for node in graph.nodes():
        if graph.in_edges(node) == []:
            return node
    return None
def findBottomNode(graph: pgv.AGraph, topNode: pgv.Node):
    visited = set()
    queue = deque([topNode])
    while queue:
        node = queue.popleft()
        visited.add(node)
        for src, dst in graph.out_edges(node):
            if dst not in visited:
                queue.append(dst)
        if len(queue) == 0:
            return node
    return None
        
# function to insert the pipeline graphs into the FSM graph
def insertPipelineGraphs(graph: pgv.AGraph, FSM: pgv.AGraph, pipelineGraphs: dict):
    for state, pipelineGraph in pipelineGraphs.items():
        assert state in FSM.nodes(), "State not found in FSM"
        assert len(FSM.out_edges(state)) <= 1, "More than one edge found"
        topNode = findTopNode(pipelineGraph) 
        assert topNode is not None, "Top node not found"
        bottomNode = findBottomNode(pipelineGraph, topNode)
        assert bottomNode is not None, "Bottom node not found"
        for node in pipelineGraph.nodes():
            FSM.add_node(node)
            FSM.get_node(node).attr["label"] = graph.get_node(node).attr["label"]
            FSM.get_node(node).attr["shape"] = graph.get_node(node).attr["shape"]
        for src, dst in pipelineGraph.edges():
            FSM.add_edge(src, dst, color="red", info=pipelineGraph.get_edge(src, dst).attr["info"])
        dstState = FSM.out_edges(state)[0][1]
        FSM.remove_edge(state, dstState)
        FSM.add_edge(state, topNode, color="red", style="dashed")
        FSM.add_edge(bottomNode, dstState, color="red", style="dashed")
        print("Pipeline graph inserted for state: {0}. Exporting new FSM graph FSM_{0}.dot".format(state))
        FSM.write("FSM_{}.dot".format(state))


# function to extract the departure states of the ctrl data CFG
def getDepartureStates(graph: pgv.AGraph, controlPaths: list, module: Module, FSM: pgv.AGraph, end_nodes: list):
    departureStates = {}
    departureStates2Ctrl = {}
    Ctrl2Data = {}
    list_ctrlOuts = []
    for ctrlNode, dataNode in controlPaths:
        Ctrl2Data[ctrlNode] = dataNode
        if not ctrlNode in list_ctrlOuts:
            list_ctrlOuts.append(ctrlNode)
    for end_node in end_nodes:
        list_ctrlOuts.append(end_node)

    currStateVar = getCurrStateVar(FSM)
    nextStateVar = getNextStateVar(FSM)
    terminateTravNodes = [ currStateVar, nextStateVar ]
    terminateTravNodes.extend(FSM.nodes())
    pipelineGraphs = {}
    for state in FSM.nodes():
        departureStates[state] = []
        departureStates2Ctrl[state] = []
        for assign in module.assignments:
            if assign.condition is None:
                continue
            if assign.expression.toString() in FSM.nodes() or assign.expression.toString() == currStateVar:
                continue
            if assign.target.toString() == nextStateVar:
                continue
            if isPatternPresent(assign.condition, currStateVar, state, "=="):
                if assign.expression.isConstant():
                    value = assign.expression.toString()
                    if value == "1'b0" or value == "0" or value == "1'd0":
                        continue
                targ, expr, cond = getAssignToNode(module, assign)
                ctrlOuts = list_ctrlOuts.copy()
                # check if the target of the condition is already in the datapath nodes
                if targ in graph.get_subgraph("cluster_data_flow").nodes():
                    dataEndPoint = targ
                    departureStates[state].append(dataEndPoint)
                    ctrlFound = False
                    for ctrl in Ctrl2Data.keys():
                        if Ctrl2Data[ctrl] == dataEndPoint and graph.in_edges(ctrl)[0][0] == cond:
                            departureStates2Ctrl[state].append(ctrl)
                            ctrlFound = True
                            break
                    assert ctrlFound, "Control node not found"
                    continue
                # check if the target of the condition is an end node
                if targ in end_nodes:
                    dataEndPoint = "endCircuit"
                    departureStates[state].append(dataEndPoint)
                    departureStates2Ctrl[state].append(targ)
                    continue
                # if this is not the case identify the control nodes that are reachable from the target node
                getDepartureStates_rec(
                    graph, targ, set(), module, ctrlOuts, terminateTravNodes,
                )
                candidateCouts = []
                for cOut in list_ctrlOuts:
                    if cOut not in ctrlOuts:
                        candidateCouts.append(cOut)
                CFG_outNode = {}
                list_outNodes = []
                for cOut in candidateCouts:
                    driverCtrl = graph.in_edges(cOut)[0][0]
                    CFG_outNode[cOut] = driverCtrl
                    if not driverCtrl in list_outNodes:
                        list_outNodes.append(driverCtrl)
                if len(list_outNodes) > 1:
                    pipelineGraph = checkPipeline(list_outNodes, currStateVar, nextStateVar, graph, module)
                    if pipelineGraph is not None:
                        assert state not in pipelineGraphs.keys(), "Pipeline graph already exists, there cannot be two pipeline graphs for the same state"
                        pipelineGraphs[state] = pipelineGraph
                for ctrl, driverCtrl in CFG_outNode.items():
                    if ctrl in Ctrl2Data.keys():
                        dataEndPoint = Ctrl2Data[ctrl]
                    elif ctrl in end_nodes:
                        dataEndPoint = "endCircuit"
                    else:
                        assert False, "Data end point associate to ctrl node not found"
                    if pipelineGraph is not None and driverCtrl in pipelineGraph.nodes():
                        if driverCtrl in pipelineGraph.nodes():
                            if not driverCtrl in departureStates.keys():
                                departureStates[driverCtrl] = []
                                departureStates2Ctrl[driverCtrl] = []
                            departureStates[driverCtrl].append(dataEndPoint)
                            departureStates2Ctrl[driverCtrl].append(ctrl)
                        else:
                            departureStates[state].append(dataEndPoint)
                            departureStates2Ctrl[state].append(ctrl)
                    else:
                        departureStates[state].append(dataEndPoint)
                        departureStates2Ctrl[state].append(ctrl)

    insertPipelineGraphs(graph, FSM , pipelineGraphs)

    return departureStates, departureStates2Ctrl

def findDrivingState(state2node: dict, module: Module, graph: pgv.AGraph, assign: Assignment):

    target, expression, condition = getAssignToNode(module, assign)
    foundState = None
    for state in state2node.keys():
        for ctrlNode in state2node[state]:
            driverCtrl = graph.in_edges(ctrlNode)[0][0]
            if driverCtrl == condition:
                foundState = state        
                break
    assert foundState is not None, "State not found"
    return foundState

# function to get the memory operations associated with a state
def getStatesMem(module: Module, graph: pgv.AGraph , enablePort: str, state2node: dict):
    assert module.isDefined(enablePort), "Output address port not found"
    numOps = 0
    statesMem = []
    for assign in module.getAssignmentsOf(enablePort):
        assert assign.expression.isConstant(), "Enable port is not a constant"
        value = assign.expression.toString()
        if value == "1'b0" or value == "0" or value == "1'd0":
            continue
        numOps += 1
        foundState = findDrivingState(state2node, module, graph, assign)
        statesMem.append(foundState)
    if numOps == 0:
        return None
    return statesMem

# function to get the states in which there is a write
def getMemWriteOpState(module: Module, graph: pgv.AGraph, writeEnablePort: str, state2node: dict):
    assert module.isDefined(writeEnablePort), "Write enable port not found"
    stateWriteOp = []
    for assign in module.getAssignmentsOf(writeEnablePort):
        assert assign.expression.isConstant(), "Write enable port is not a constant"
        value = assign.expression.toString()
        if value == "1'b0" or value == "0" or value == "1'd0":
            continue
        foundState = findDrivingState(state2node, module, graph, assign)
        stateWriteOp.append(foundState)
    return stateWriteOp

# function to add a store operation to the CDFG
def addStoreOps(CDFG: pgv.AGraph, graph: pgv.AGraph, module: Module, state2node: dict, statesWriteOp: list, portOutAddress: str, portToMemory: str, node_name_template: str):
    state2addr = {}
    state2data = {}
    for assignment in module.getAssignmentsOf(portOutAddress):
        if assignment.condition is None:
            continue
        state = findDrivingState(state2node, module, graph, assignment)
        if state not in statesWriteOp:
            continue
        target, expression, condition = getAssignToNode(module, assignment)
        state2addr[state] = expression
    for assignment in module.getAssignmentsOf(portToMemory):
        if assignment.condition is None:
            continue
        state = findDrivingState(state2node, module, graph, assignment)
        if state not in statesWriteOp:
            continue
        target, expression, condition = getAssignToNode(module, assignment)
        state2data[state] = expression
    idOp = 0
    storeOpsNames = []
    for state in statesWriteOp:
        node_name = node_name_template + "_" + str(idOp)
        assert state in state2addr.keys(), "Address not found"
        assert state in state2data.keys(), "Data not found"
        addr = state2addr[state]
        data = state2data[state]

        CDFG.remove_edge(addr, portOutAddress)
        CDFG.remove_edge(data, portToMemory)
        CDFG.add_edge(addr, node_name, color="red")
        CDFG.add_edge(data, node_name, color="red")

        storeOpsNames.append(node_name)
        idOp += 1

    return storeOpsNames

# function to add a load operation to the CDFG
def addLoadOps(CDFG: pgv.AGraph, graph: pgv.AGraph, module: Module, state2node: dict, statesReadOp: list, portOutAddress: str, portFromMemory: str, node_name_template: str):
    state2addr = {}
    state2data = {}
    for assignment in module.getAssignmentsOf(portOutAddress):
        if assignment.condition is None:
            continue
        state = findDrivingState(state2node, module, graph, assignment)
        if state not in statesReadOp:
            continue
        target, expression, condition = getAssignToNode(module, assignment)
        state2addr[state] = expression
    
    idOp = 0
    loadOpNames = []
    for state in statesReadOp:
        node_name = node_name_template + "_" + str(idOp)
        assert state in state2addr.keys(), "Address not found"
        addr = state2addr[state]
        CDFG.remove_edge(addr, portOutAddress)
        CDFG.add_edge(addr, node_name, color="red")
        infoFromMemory = CDFG.out_edges(portFromMemory)[0][1]
        CDFG.add_edge(node_name, infoFromMemory, color="red")
        CDFG.remove_edge(portFromMemory, infoFromMemory)        

        loadOpNames.append(node_name)
        idOp += 1

    return loadOpNames

# function to remove the memory nodes from the CDFG
def removeMemNodes(CDFG: pgv.AGraph, memoryNodes: dict):
    for keyword, node in memoryNodes.items():
        if keyword != "regex_memory" and keyword != "inAddress":
            for src, dst in CDFG.in_edges(node):
                CDFG.remove_edge(src, dst)
                CDFG.remove_node(src)
            CDFG.remove_node(node)

# function to get the conversion from the state name to the distance from the start state
def getStateNameToStateDistance(FSM: pgv.AGraph):
    startState = None
    for state in FSM.nodes():
        if "comment" in FSM.get_node(state).attr.keys() and FSM.get_node(state).attr["comment"] == "Start":
            startState = state
            break
    assert startState is not None, "Start state not found"
    visited = set()
    queue1 = deque([startState])
    distance = 0
    stateName2Distance = { startState: 0 }
    while queue1:
        queue2 = queue1.copy()
        while queue2:
            current_state = queue2.popleft()
            queue1.popleft()
            visited.add(current_state)
            for src, dst in FSM.out_edges(current_state):
                if dst not in visited:
                    queue1.append(dst)
                    stateName2Distance[dst] = distance + 1
        distance += 1
    return stateName2Distance

# function to add the dependencies between the memory operations
def addInterMemoryDep(CDFG: pgv.AGraph, FSM: pgv.AGraph ,statesWriteOp: list, storeOps: list, statesReadOp: list, loadOps: list):
    stateName2Distance = getStateNameToStateDistance(FSM)
    tmpStatesWriteOp = []
    for state in statesWriteOp:
        tmpStatesWriteOp.append(stateName2Distance[state])
    tmpStatesReadOp = []
    for state in statesReadOp:
        tmpStatesReadOp.append(stateName2Distance[state])
    idStoreOp = 0
    idLoadOp = 0
    lastOps = []
    while len(tmpStatesWriteOp) > 0 or len(tmpStatesReadOp) > 0:
        if len(tmpStatesReadOp) == 0:
            tmpStatesWriteOp.pop(0)
            storeOp = storeOps[idStoreOp]
            idStoreOp += 1
            if len(lastOps) > 0:
                for lastOp in lastOps:
                    CDFG.add_edge(lastOp, storeOp, color="red", style="dashed")
                    # in order to avoid any overlapping also the loopback with the II has to be added 
                    CDFG.add_edge(storeOp, lastOp, color="red", style="dashed", comment="II - 1")
            lastOps = [storeOp]
            continue
        elif len(tmpStatesWriteOp) == 0:
            tmpStatesReadOp.pop(0)
            loadOp = loadOps[idLoadOp]
            idLoadOp += 1
            if len(lastOps) > 0:
                for lastOp in lastOps:
                    CDFG.add_edge(lastOp, loadOp, color="red", style="dashed")
                    # in order to avoid any overlapping also the loopback with the II has to be added 
                    CDFG.add_edge(loadOp, lastOp, color="red", style="dashed", comment="II - 1")
            lastOps = [loadOp]
            continue
        if tmpStatesWriteOp[0] == tmpStatesReadOp[0]:
            tmpStatesWriteOp.pop(0)
            tmpStatesReadOp.pop(0)
            if len(lastOps) > 0:
                storeOp = storeOps[idStoreOp]
                loadOp = loadOps[idLoadOp]
                for lastOp in lastOps:
                    CDFG.add_edge(lastOp, storeOp, color="red", style="dashed")
                    CDFG.add_edge(lastOp, loadOp, color="red", style="dashed")
                    # in order to avoid any overlapping also the loopback with the II has to be added 
                    CDFG.add_edge(storeOp, lastOp, color="red", style="dashed", comment="II - 1")
                    CDFG.add_edge(loadOp, lastOp, color="red", style="dashed", comment="II - 1")
            lastOps = [storeOp, loadOp]
            idStoreOp += 1
            idLoadOp += 1
            continue
        if tmpStatesWriteOp[0] < tmpStatesReadOp[0]:
            tmpStatesWriteOp.pop(0)
            storeOp = storeOps[idStoreOp]
            idStoreOp += 1
            if len(lastOps) > 0:
                for lastOp in lastOps:
                    CDFG.add_edge(lastOp, storeOp, color="red", style="dashed")
                    # in order to avoid any overlapping also the loopback with the II has to be added 
                    CDFG.add_edge(storeOp, lastOp, color="red", style="dashed", comment="II - 1")
            lastOps = [storeOp]
            continue
        if tmpStatesWriteOp[0] > tmpStatesReadOp[0]:
            tmpStatesReadOp.pop(0)
            loadOp = loadOps[idLoadOp]
            idLoadOp += 1
            if len(lastOps) > 0:
                for lastOp in lastOps:
                    CDFG.add_edge(lastOp, loadOp, color="red", style="dashed")
                    # in order to avoid any overlapping also the loopback with the II has to be added
                    CDFG.add_edge(loadOp, lastOp, color="red", style="dashed", comment="II - 1")
            lastOps = [loadOp]
            continue

        assert False, "Error in the memory operations"
    
    return

# function to merge memory ports of the CDFG
def memory_merge(module: Module, CDFG: pgv.AGraph, FSM: pgv.AGraph, graph: pgv.AGraph , state2node: dict, memory_keywords: dict):

    regex_memory = memory_keywords["regex_memory"]

    for _idMemReg in range(len(regex_memory)):
        regOutAddress = regex_memory[_idMemReg]
        memories = {}
        for node in CDFG.nodes():
            if re.match(regOutAddress, node):
                match = re.search(regOutAddress, node)
                memory_name = match.group("memory_name")
                memory_id = match.group("memory_id")
                if memory_name not in memories.keys():
                    memories[memory_name] = []
                if memory_id not in memories[memory_name]:
                    memories[memory_name].append(memory_id)
        if len(memories) > 0:
            idMemReg = _idMemReg
            break
    assert len(memories) > 0, "No memory ports found"
    for memory_name in memories.keys():
        for memory_id in memories[memory_name]:
            memoryNodes = {}
            for node in CDFG.nodes():
                for keyword in memory_keywords.keys():
                    memoryNode = memory_keywords[keyword][idMemReg].replace("MEMORY_NAME", memory_name).replace("MEMORY_ID", memory_id)
                    if memoryNode == node.get_name():
                        assert keyword not in memoryNodes.keys(), "Memory node already exists"
                        memoryNodes[keyword] = node
            # assert that memory nodes and memory keywords have the same length apart from the regex
            assert len(memoryNodes) >= len(memory_keywords) - 3, "Memory nodes not found"
            statesMem = getStatesMem(module, graph , memoryNodes["enable"], state2node)
            if statesMem is None:
                removeMemNodes(CDFG, memoryNodes)
                continue
            # identify the states in which there is a write operation, the remaining states in statesMem are read operations
            if "writeEnable" in memoryNodes.keys():
                statesWriteOp = getMemWriteOpState(module, graph, memoryNodes["writeEnable"], state2node)
            else:
                statesWriteOp = []
            statesReadOp = [state for state in statesMem if state not in statesWriteOp]

            if len(statesWriteOp) > 0:
                newStoreOps = addStoreOps(CDFG, graph, module, state2node, statesWriteOp, memoryNodes["outAddress"], memoryNodes["inMemory"], "store_{0}_{1}".format(memory_name, memory_id))
            if len(statesReadOp) > 0:
                newLoadOps = addLoadOps(CDFG, graph, module, state2node, statesReadOp, memoryNodes["outAddress"], memoryNodes["outMemory"], "load_{0}_{1}".format(memory_name, memory_id))

            # add edges for dependencies across the memory operations
            if len(statesWriteOp) > 0 and len(statesReadOp) > 0:
                addInterMemoryDep(CDFG, FSM, statesWriteOp, newStoreOps, statesReadOp, newLoadOps)

            # remove the nodes still existing in the CDFG and all the nodes connected to them
            removeMemNodes(CDFG, memoryNodes)

    # remove byteena node if present
    allNodes = CDFG.nodes()
    for node in allNodes:
        if "byteena" in node:
            for src, dst in CDFG.in_edges(node):
                CDFG.remove_edge(src, dst)
                CDFG.remove_node(src)
            CDFG.remove_node(node)

# function to replace the muxes in the CDFG with phis
def replaceMuxes(CDFG: pgv.AGraph, module: Module, graph: pgv.AGraph, state2node: dict):
    for node in CDFG.nodes():
        if module.isDefined(node):
            assignemnts = module.getAssignmentsOf(node)
            if len(assignemnts) > 1:
                CDFG.get_node(node).attr["shape"] = "diamond"
                CDFG.get_node(node).attr["label"] = "PHI"
                assert len(CDFG.in_edges(node)) > 1, "The node should have more than one input"

# function to reorder the states to merge in the FSM
def reorderStates2Merge( states2merge: dict ):
    graph = {}
    indegree = {}

    # Initialize the graph and indegree count for each node
    nodes = set(states2merge.keys()).union(set(states2merge.values()))
    for node in nodes:
        indegree[node] = 0
        graph[node] = []
    
    for src, dst in states2merge.items():
        graph[dst].append(src)
        indegree[src] += 1

    sorted_nodes = []    
    # Initialize the queue with the nodes with indegree 0
    queue = deque([node for node in indegree.keys() if indegree[node] == 0])
    while queue:
        node = queue.popleft()
        sorted_nodes.append(node)
        for dst in graph[node]:
            indegree[dst] -= 1
            if indegree[dst] == 0:
                queue.append(dst)
    
    assert len(sorted_nodes) == len(nodes), "Cycle found in the graph"

    result = []
    for node in sorted_nodes:
        for key, value in states2merge.items():
            if value == node:
                result.append((key, value))

    return result

# function to merge consecutive pipeline states
def mergeConsecutivePipelineStates(FSM: pgv.AGraph, departureStates: dict, departureStates2Ctrl , arrivalStates: list):

    mergedStates = {}
    for edge in FSM.edges():
        if "info" in FSM.get_edge(edge[0], edge[1]).attr.keys():
            info = FSM.get_edge(edge[0], edge[1]).attr["info"]
            if "NumRegs" in info:
                numRegs = int(info.split("=")[1])
                if numRegs == 0:
                    mergedStates[edge[0]] = edge[1] 

    reorderedMergedStates = reorderStates2Merge(mergedStates)

    for src, dst in reorderedMergedStates:
        # remove dst state
        FSM.remove_edge(src, dst)
        for out in FSM.out_edges(dst):
            FSM.add_edge(src, out[1], color="blue", style="dashed")
            if "info" in FSM.get_edge(dst, out[1]).attr.keys():
                FSM.get_edge(src, out[1]).attr["info"] = FSM.get_edge(dst, out[1]).attr["info"]
            FSM.remove_edge(dst, out[1])
        FSM.remove_node(dst)

        list2move = departureStates[dst]
        departureStates[src].extend(list2move)
        del departureStates[dst]
        list2move = departureStates2Ctrl[dst]
        departureStates2Ctrl[src].extend(list2move)
        del departureStates2Ctrl[dst]
        copy_arrival = arrivalStates.copy()
        for dataSrcNode, arrivalState in copy_arrival:
            if arrivalState == dst:
                arrivalStates.remove((dataSrcNode, arrivalState))
                arrivalStates.append((dataSrcNode, src))

    FSM.write("FSM_merged.dot")

# function to remove duplicate variables in the CDFG
def removeDuplicateVars(CDFG: pgv.AGraph):
    nodes = CDFG.nodes()
    for node in nodes:
        out_nodes = []
        for src, dst in CDFG.out_edges(node):
            if dst not in out_nodes:
                out_nodes.append(dst)
        if len(CDFG.out_edges(node)) >= 1 and len(out_nodes) == 1:
            if isVarNode(CDFG.get_node(node)) and isVarNode(CDFG.get_node(out_nodes[0])):
                # ensure no multiplier is removed
                if ("mult" in node and not("mult" in out_nodes[0])) or ("mult" in out_nodes[0] and not("mult" in node)):
                    continue
                src = node
                dst = out_nodes[0]
                for src2, dst2 in CDFG.in_edges(src):
                    if (src2, dst) not in CDFG.edges():
                        CDFG.add_edge(src2, dst, color=CDFG.get_edge(src2, src).attr["color"], style=CDFG.get_edge(src2, src).attr["style"])
                    else:
                        #print("Skipped {0} -> {1}".format(src2, dst))
                        pass
                CDFG.remove_node(src)

# function to connect the multiplication inputs and outputs in the CDFG
def mult_connect(CDFG: pgv.AGraph):
    nodes = CDFG.nodes()
    foundMult = False
    for node in nodes:
        if "mult" in node:
            foundMult = True
            break
    if not foundMult:
        return
    multNames = []
    for node in nodes:
        if "mult" in node and "_datab" in node:
            multName = node.replace("_datab", "")
            multNames.append(multName)
    for multName in multNames:
        inputA = None
        inputB = None
        output = None
        for node in nodes:
            if multName in node:
                if "_datab" in node:
                    inputB = node
                elif "_dataa" in node:
                    inputA = node
                elif "_result" in node:
                    assert output is None, "Output already found"
                    output = node

        assert inputA is not None, "Input A not found"
        assert inputB is not None, "Input B not found"
        assert output is not None, "Output not found"
        CDFG.add_edge(inputA, output, color="red")
        CDFG.add_edge(inputB, output, color="red")

# function to build the original CDFG with the extracted data flow
def buildOriginalCDFG(graph: pgv.AGraph, module: Module, FSM: pgv.AGraph, end_nodes: list, memory_keywords: dict):
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


    for node in CDFG.nodes():
        name = graph.get_node(node).attr["label"]
        CDFG.get_node(node).attr["label"] = name
        shape = graph.get_node(node).attr["shape"]
        CDFG.get_node(node).attr["shape"] = shape

    # departure states should be computed first since they identify potential pipeline graphs and insert them in the FSM
    departureStates, departureStates2Ctrl = getDepartureStates(graph, outCtrlInDataWire, module, FSM, end_nodes)
    arrivalStates = getArrivalStates(graph, inCtrlOutDataWire, module, end_nodes, FSM)
    for dataSrcNode, arrivalState in arrivalStates:
        assert arrivalState in departureStates.keys() or arrivalState in end_nodes, "Arrival state not found"
        if arrivalState in end_nodes:
            dataDstNodes = ["endCircuit"]
        else:
            dataDstNodes = departureStates[arrivalState]
        for dataDstNode in dataDstNodes:
            edge = (dataSrcNode.get_name(), dataDstNode)
            if not edge in CDFG.edges():
                CDFG.add_edge(dataSrcNode.get_name(), dataDstNode, color="red", style="dashed")
        #print(f"Data node {dataSrcNode.get_name()} -> {dataDstNodes}")
    # the pipeline states with no registers across them should be merged since do not represent real states
    mergeConsecutivePipelineStates(FSM, departureStates, departureStates2Ctrl , arrivalStates)
    memory_merge(module, CDFG, FSM, graph, departureStates2Ctrl, memory_keywords)

    removeDuplicateVars(CDFG)
    replaceMuxes(CDFG, module, graph, departureStates2Ctrl)

    return CDFG

# function to generate header of the verilog file
def generateHeader(ports: list):
    header = "module top(\n"
    for port in ports:
        header += port + ", \n"
    header = header[:-3]
    header += "\n);\n"  
    return header  

# function to generate the variables that are used in the CDFG
def generateVariablesDef(inputs: dict, outputs: dict, vars: dict, dip_dependencies: dict):
    text = ""
    for input in inputs.keys():
        if inputs[input] == 1:
            text += "input {0};\n".format(input)
            dip_dependencies[input] = input
        else:
            bitwidth = inputs[input]
            text += "input [{0}:0] {1};\n".format(bitwidth - 1, input)
            for i in range(bitwidth):
                dip_dependencies[input + "[" + str(i) + "]"] = input

    for output in outputs.keys():
        if outputs[output] == 1:
            text += "output {0};\n".format(output)
            dip_dependencies[output] = output
        else:
            bitwidth = outputs[output]
            text += "output [{0}:0] {1};\n".format(bitwidth - 1, output)
            for i in range(bitwidth):
                dip_dependencies[output + "[" + str(i) + "]"] = output

    for var in vars.keys():
        if vars[var] == 1:
            text += "wire {0};\n".format(var)
        else:
            text += "wire [{0}:0] {1};\n".format(vars[var] - 1, var)
    return text

def isConst(node: str):
    try:
        v = int(node)
        return True
    except:
        pass
    if "'b" in node or "'d" in node:
        return True
    return False

# function to find the input root of a node
def getInputRoot(CDFG: pgv.AGraph, node: pgv.Node):

    if CDFG.get_node(node).attr["shape"] != "ellipse":
        return node
    if CDFG.in_edges(node) == []:
        return CDFG.get_node(node).attr["label"]
    value = CDFG.get_node(node).attr["label"]
    if value == "+" or value == "-" or value == "*" or value == "/" or value == "==":
        if value == "-" and len(CDFG.in_edges(node)) == 1:
            return "(-" + getInputRoot(CDFG, CDFG.in_edges(node)[0][0]) + ")"
        lhs = getInputRoot(CDFG, CDFG.in_edges(node)[0][0])
        rhs = getInputRoot(CDFG, CDFG.in_edges(node)[1][0])
        return "({0} {1} {2})".format(lhs, value, rhs)
    elif value == "~":
        return "{0}({1})".format(value, getInputRoot(CDFG, CDFG.in_edges(node)[0][0]))
    elif value == ">>" or value == "<<" or value == ">>>":
        lhs = getInputRoot(CDFG, CDFG.in_edges(node)[0][0])
        rhs = getInputRoot(CDFG, CDFG.in_edges(node)[1][0])
        if isConst(rhs):
            return "({0} {1} {2})".format(lhs, value, rhs)
        else:
            return "({0} {1} {2})".format(rhs, value, lhs)
    elif value == "{{{}}}":
        lhs = getInputRoot(CDFG, CDFG.in_edges(node)[0][0])
        rhs = getInputRoot(CDFG, CDFG.in_edges(node)[1][0])
        if isConst(rhs):
            return "({" + str(rhs) + "," + str(lhs) + "})"
        else:
            return "({" + str(lhs) + "," + str(rhs) + "})"
    elif value == "[]":
        numInputs = len(CDFG.in_edges(node))
        assert numInputs == 3 or numInputs == 2, "Number of inputs not supported"
        input1 = getInputRoot(CDFG, CDFG.in_edges(node)[0][0])
        input2 = getInputRoot(CDFG, CDFG.in_edges(node)[1][0])
        if numInputs == 3:
            input3 = getInputRoot(CDFG, CDFG.in_edges(node)[2][0])
            input3Int = isConst(input3)
        input1Int = isConst(input1)
        input2Int = isConst(input2)
        if numInputs == 3:
            if input1Int:
                if input2Int:
                    return "{0}[{1}:{2}]".format(input3, input2 if int(input2) > int(input1) else input1, input1 if int(input2) > int(input1) else input2)
                else:
                    assert input3Int, "At least 2 of the 3 inputs should be constants"
                    return "{0}[{1}:{2}]".format(input2, input3 if int(input3) > int(input1) else input1, input1 if int(input3) > int(input1) else input3)
            else:
                if input2Int:
                    return "{0}[{1}:{2}]".format(input1, input3 if int(input3) > int(input2) else input2, input2 if int(input3) > int(input2) else input3)
                else:
                    assert False, "At least 2 of the 3 inputs should be constants"
        else:
            if input1Int:
                if input2Int:
                    assert False, "Only 1 of the 2 inputs should not be constants"
                else:
                    return "{0}[{1}]".format(input2, input1)
            else:
                if input2Int:
                    return "{0}[{1}]".format(input1, input2)
                else:
                    assert False, "Only 1 of the 2 inputs should be constants"
    elif value == "{n{}}":
        lhs = getInputRoot(CDFG, CDFG.in_edges(node)[0][0])
        rhs = getInputRoot(CDFG, CDFG.in_edges(node)[1][0])
        if isConst(rhs):
            return "({" + str(rhs) + "{" + str(lhs) + "}" + "})"
        else:
            return "({" + str(lhs) + "{" + str(rhs) + "}"+ "})"
    else:
        assert False, "Node not recognized"

# function to generate assign inside verilog module
def generateAssigns(CDFG: pgv.AGraph, module: Module):

    assigns = ""

    for node in CDFG.nodes():
        if CDFG.get_node(node).attr["shape"] != "ellipse":
            isPhi = CDFG.get_node(node).attr["label"] == "PHI"
            numDataEdges = 0
            for src, dst in CDFG.in_edges(node):
                if CDFG.get_edge(src, dst).attr["color"] != "red" and CDFG.get_edge(src, dst).attr["style"] != "dashed":
                    numDataEdges += 1
            assert numDataEdges <= 1 or isPhi, "Node should have one input"
            if CDFG.in_edges(node) == []:
                continue
            assignment = getInputRoot(CDFG, CDFG.in_edges(node)[0][0])
            if isPhi:
                assignment2 = getInputRoot(CDFG, CDFG.in_edges(node)[1][0])
                cond = getInputRoot(CDFG, CDFG.in_edges(node)[2][0])
                assigns += "assign {0} = {1} ? {2} : {3};\n".format(node, cond, assignment, assignment2)
            else:
                assigns += "assign {0} = {1};\n".format(node, assignment)
    
    return assigns

# function to get the width of node
def getWidth(node: pgv.Node, module: Module):
    rangeNode = module.getPort(node).getRange()
    if rangeNode is None:
        return 1
    rightConstant = int(rangeNode.end.variable_name) 
    leftConstant = int(rangeNode.start.variable_name)
    return leftConstant - rightConstant + 1

# function to extract the inputs
def getPIs(CDFG: pgv.AGraph, module: Module):
    PIs = {}
    for node in CDFG.nodes():
        if CDFG.in_edges(node) == []:
            if CDFG.get_node(node).attr["shape"] != "box":
                continue
            PIs[node] = getWidth(node, module)
    return PIs

# function to extract the outputs
def getPOs(CDFG: pgv.AGraph, module: Module):
    POs = {}
    for node in CDFG.nodes():
        if CDFG.out_edges(node) == []:
            if CDFG.get_node(node).attr["shape"] != "box" and not "endCircuit" in node:
                continue
            if "endCircuit" in node:
                POs[node] = 1
                CDFG.get_node(node).attr["shape"] = "box"
                assert len(CDFG.in_edges(node)) == 1, "End node should have one input"
                srcEnd = CDFG.in_edges(node)[0][0]
                CDFG.get_edge(srcEnd, node).attr["style"] = "solid"
                continue
            POs[node] = getWidth(node, module)
    return POs

# function to update the cip dependencies with the new nodes
def update_cip_dep(old_src, old_dst, new_src, new_dst, new_delay, cip_dependencies):

    tmp_cip_dependencies = cip_dependencies.copy()
    foundDep = False
    for dst, src, delay in tmp_cip_dependencies:
        if src == old_src and dst == old_dst:
            foundDep = True
            cip_dependencies.remove((dst, src, delay))
            if isinstance(delay, str) and not "II" in delay:
                cip_dependencies.append((new_dst, new_src, new_delay))
            else:
                cip_dependencies.append((new_dst, new_src, delay))
    if not foundDep:
        cip_dependencies.append((new_dst, new_src, new_delay))

# function to add new PIs and POs to the CDFG for the memory units
def addMemoryUnitsPorts(CDFG: pgv.AGraph, module: Module, memory_keywords: dict, memoryIdx: int, cip_dependencies: list):

    additionalPIs = {}
    additionalPOs = {}
    nodes = CDFG.nodes()
    for node in nodes:
        if "load" in node:
            fromMem = memory_keywords["outMemory"][memoryIdx]
            fromMem = fromMem.replace("MEMORY_NAME", node.split("_")[1]).replace("MEMORY_ID", node.split("_")[2])
            fromMemNode = node + "_fromMem"
            additionalPIs[fromMemNode] = getWidth(fromMem, module)
            addr = memory_keywords["outAddress"][memoryIdx]
            addr = addr.replace("MEMORY_NAME", node.split("_")[1]).replace("MEMORY_ID", node.split("_")[2])
            addrNode = node + "_addr"
            additionalPOs[addrNode] = getWidth(addr, module)
            CDFG.add_node(fromMemNode, shape="box")
            CDFG.add_node(addrNode, shape="box")
            noCIPEdges = 0
            for src, dst in CDFG.in_edges(node):
                if CDFG.get_edge(src, dst).attr["style"] == "dashed" and CDFG.get_edge(src, dst).attr["color"] == "red":
                    continue
                noCIPEdges += 1
            assert noCIPEdges == 1, "Load node should have one input"
            noCIPEdges = 0
            for src, dst in CDFG.out_edges(node):
                if CDFG.get_edge(src, dst).attr["style"] == "dashed" and CDFG.get_edge(src, dst).attr["color"] == "red":
                    continue
                noCIPEdges += 1
            assert noCIPEdges == 1, "Load node should have one output"
            # IMPORTANT: the address is the first important and the data is the first output
            addrReq = CDFG.in_edges(node)[0][0]
            dataAnswer = CDFG.out_edges(node)[0][1]
            CDFG.add_edge(addrReq, addrNode, color="red")
            CDFG.add_edge(fromMemNode, dataAnswer, color="red")
            cip_dependencies.append((fromMemNode, addrNode, 1))
            for src, dst in CDFG.in_edges(node):
                if src != addrReq:
                    assert CDFG.get_edge(src, dst).attr["style"] == "dashed" and CDFG.get_edge(src, dst).attr["color"] == "red", "Load node should have one input that is not dashed"
                    CDFG.add_edge(src, addrNode, color="red", style="dashed")
                    if "comment" in CDFG.get_edge(src, dst).attr.keys() and "II" in CDFG.get_edge(src, dst).attr["comment"]:
                        distance_value = CDFG.get_edge(src, dst).attr["comment"]
                    else:
                        distance_value = 1
                    update_cip_dep(src, dst, src, addrNode, distance_value, cip_dependencies)
            for src, dst in CDFG.out_edges(node):
                if dst != dataAnswer:
                    assert CDFG.get_edge(src, dst).attr["style"] == "dashed" and CDFG.get_edge(src, dst).attr["color"] == "red", "Load node should have one output that is not dashed"
                    CDFG.add_edge(fromMemNode, dst, color="red", style="dashed")
                    if "comment" in CDFG.get_edge(src, dst).attr.keys() and "II" in CDFG.get_edge(src, dst).attr["comment"]:
                        distance_value = CDFG.get_edge(src, dst).attr["comment"]
                    else:
                        distance_value = 1
                    update_cip_dep(src, dst, fromMemNode, dst, distance_value, cip_dependencies)
            CDFG.remove_node(node)
        if "store" in node:
            toMem = memory_keywords["inMemory"][memoryIdx]
            toMem = toMem.replace("MEMORY_NAME", node.split("_")[1]).replace("MEMORY_ID", node.split("_")[2])
            toMemNode = node + "_toMem"
            additionalPOs[toMemNode] = getWidth(toMem, module)
            addr = memory_keywords["outAddress"][memoryIdx]
            addr = addr.replace("MEMORY_NAME", node.split("_")[1]).replace("MEMORY_ID", node.split("_")[2])
            addrNode = node + "_addr"
            additionalPOs[addrNode] = getWidth(addr, module)
            noCIPEdges = 0
            for src, dst in CDFG.in_edges(node):
                if CDFG.get_edge(src, dst).attr["style"] == "dashed" and CDFG.get_edge(src, dst).attr["color"] == "red":
                    continue
                noCIPEdges += 1
            assert noCIPEdges == 2, "Store node should have two inputs"
            # IMPORTANT: the address is the first input and the data is the second input
            addrReq = CDFG.in_edges(node)[0][0]
            dataReq = CDFG.in_edges(node)[1][0]
            CDFG.add_edge(addrReq, addrNode, color="red")
            CDFG.add_edge(dataReq, toMemNode, color="red")
            for src, dst in CDFG.in_edges(node):
                if src != addrReq and src != dataReq:
                    assert CDFG.get_edge(src, dst).attr["style"] == "dashed" and CDFG.get_edge(src, dst).attr["color"] == "red", "Store node should have two inputs that are not dashed"
                    CDFG.add_edge(src, addrNode, color="red", style="dashed")
                    CDFG.add_edge(src, toMemNode, color="red", style="dashed")
                    if "comment" in CDFG.get_edge(src, dst).attr.keys() and "II" in CDFG.get_edge(src, dst).attr["comment"]:
                        distance_value = CDFG.get_edge(src, dst).attr["comment"]
                    else:
                        distance_value = 1
                    update_cip_dep(src, dst, src, addrNode, distance_value, cip_dependencies)
                    update_cip_dep(src, dst, src, toMemNode, distance_value, cip_dependencies)
            for src, dst in CDFG.out_edges(node):
                assert CDFG.get_edge(src, dst).attr["style"] == "dashed" and CDFG.get_edge(src, dst).attr["color"] == "red", "Store node should have one output that is dashed"
                CDFG.add_edge(toMemNode, dst, color="red", style="dashed")
                CDFG.add_edge(addrNode, dst, color="red", style="dashed")
                if "comment" in CDFG.get_edge(src, dst).attr.keys() and "II" in CDFG.get_edge(src, dst).attr["comment"]:
                    distance_value = CDFG.get_edge(src, dst).attr["comment"]
                else:
                    distance_value = 1
                update_cip_dep(src, dst, toMemNode, dst, distance_value, cip_dependencies)
                update_cip_dep(src, dst, addrNode, dst, distance_value, cip_dependencies)
            CDFG.remove_node(node)

    return additionalPIs, additionalPOs

# function to add new PIs and POs to the CDFG for the multi-latency operations
# this function assumes all the inputs and outputs of the multi-latency operations are present in the CDFG
def addMultiLatencyPorts_2(CDFG: pgv.AGraph, module: Module, cip_dependencies: list):
    
    additionalPIs = {}
    additionalPOs = {}
    nodes = CDFG.nodes()
    mult_nodes = {}
    for node in nodes:
        if "mult" in node and "_datab" in node:
            multName = node.replace("_datab", "")
            assert multName not in mult_nodes.keys(), "Mult node already found"
            mult_nodes[multName] = {}
    for node in nodes:
        if "mult" in node:
            if "_dataa" in node:     
                multName = node.replace("_dataa", "")
                assert multName in mult_nodes.keys(), "Mult node not found"
                assert "input1" not in mult_nodes[multName].keys(), "Data A already found"
                mult_nodes[multName]["input1"] = node           
                additionalPOs[node] = getWidth(node, module)
                for src, dst in CDFG.out_edges(node):
                    CDFG.remove_edge(node, dst)
            elif "_datab" in node:
                multName = node.replace("_datab", "")
                assert multName in mult_nodes.keys(), "Mult node not found"
                assert "input2" not in mult_nodes[multName].keys(), "Data B already found"
                mult_nodes[multName]["input2"] = node
                additionalPOs[node] = getWidth(node, module)
                for src, dst in CDFG.out_edges(node):
                    CDFG.remove_edge(node, dst)
            elif "_result" in node:
                multName = node.replace("_result", "")
                assert multName in mult_nodes.keys(), "Mult node not found"
                assert "result" not in mult_nodes[multName].keys(), "Result already found"
                mult_nodes[multName]["result"] = node
                additionalPIs[node] = getWidth(node, module)
                for src, dst in CDFG.in_edges(node):
                    CDFG.remove_edge(src, node)

    memLatency = 4
    for multName in mult_nodes.keys():
        assert "input1" in mult_nodes[multName].keys(), "Input 1 not found"
        assert "input2" in mult_nodes[multName].keys(), "Input 2 not found"
        assert "result" in mult_nodes[multName].keys(), "Result not found"
        cip_dependencies.append((mult_nodes[multName]["result"] , mult_nodes[multName]["input1"], memLatency))
        cip_dependencies.append((mult_nodes[multName]["result"] , mult_nodes[multName]["input2"], memLatency))

    return additionalPIs, additionalPOs

# function to add new PIs and POs to the CDFG for the multi-latency operations
# this function assumes that there is only one node for the entire multi-latency operation
def addMultiLatencyPorts(CDFG: pgv.AGraph, module: Module, cip_dependencies: list):

    additionalPIs = {}
    additionalPOs = {}
    nodes = CDFG.nodes()
    mult_nodes = {}
    for node in nodes:
        if "mult" in node:
            if "_out_actual" in node:     
                multName = node.replace("_out_actual", "")
                assert not multName in mult_nodes.keys(), "Mult node already found"
                mult_nodes[multName] = {}
                input1 = multName + "_in1"
                input2 = multName + "_in2"
                result = multName + "_result"
                mult_nodes[multName]["input1"] = input1
                mult_nodes[multName]["input2"] = input2
                mult_nodes[multName]["result"] = result           
                additionalPOs[input1] = getWidth(node, module)
                additionalPOs[input2] = getWidth(node, module)
                additionalPIs[result] = getWidth(node, module)
                CDFG.add_node(input1, shape="box")
                CDFG.add_node(input2, shape="box")
                CDFG.add_node(result, shape="box")
                for src, dst in CDFG.out_edges(node):
                    CDFG.add_edge(result, dst, color="red")
                assert len(CDFG.in_edges(node)) == 2, "Mult node should have two inputs"
                input1Src = CDFG.in_edges(node)[0][0]
                input2Src = CDFG.in_edges(node)[1][0]
                CDFG.add_edge(input1Src, input1, color="red")
                CDFG.add_edge(input2Src, input2, color="red")
                CDFG.remove_node(node)

    memLatency = 4
    for multName in mult_nodes.keys():
        assert "input1" in mult_nodes[multName].keys(), "Input 1 not found"
        assert "input2" in mult_nodes[multName].keys(), "Input 2 not found"
        assert "result" in mult_nodes[multName].keys(), "Result not found"
        cip_dependencies.append((mult_nodes[multName]["result"] , mult_nodes[multName]["input1"], memLatency))
        cip_dependencies.append((mult_nodes[multName]["result"] , mult_nodes[multName]["input2"], memLatency))

    return additionalPIs, additionalPOs

# function to extract variables from the CDFG
def extractVariables(CDFG: pgv.AGraph, module: Module, PIs: list, POs: list):
    variables = {}
    for node in CDFG.nodes():
        if CDFG.get_node(node).attr["shape"] == "ellipse":
            continue
        if node in PIs or node in POs:
            continue
        variables[node] = getWidth(node, module)
    return variables

# function to find the control edge in a loop that does not drive a PHI
def findControlEdge(CDFG: pgv.AGraph, loop: list):
    for id in range(len(loop)):
        src = loop[id]
        dst = loop[(id+1) % len(loop)]
        if CDFG.get_node(dst).attr["label"] != "PHI":
            if CDFG.get_edge(src, dst).attr["style"] == "dashed" and CDFG.get_edge(src, dst).attr["color"] == "red":
                return (src, dst)
    return None

# function to break the loops in the CDFG if there are PHIs (the other possible scenario is circular dependencies)
def breakLoopsPhis(CDFG: pgv.AGraph, module: Module, cip_dependencies: list):

    additionalPIs = {}
    additionalPOs = {}
    nxGraph = nx.DiGraph(CDFG.copy())
    cycle = nx.simple_cycles(nxGraph)
    loopsNodes = sorted(cycle) if cycle is not None else None
    while loopsNodes is not None and len(loopsNodes) > 0 and loopsNodes != []:
        loop = loopsNodes[0]
        controlEdge =  findControlEdge(CDFG, loop)
        if controlEdge is not None:
            nxGraph.remove_edge(controlEdge[0], controlEdge[1])
            cycle = nx.simple_cycles(nxGraph)
            if cycle == [] or cycle is None:
                break
            loopsNodes = sorted(cycle)
            continue
        idxPhi = -1
        for id in range(len(loop)):
            node = loop[id]
            if "PHI" in CDFG.get_node(node).attr["label"]:
                idxPhi = id
        if idxPhi == -1:
            nxGraph.remove_edge(loop[0], loop[1])
        else:
            driverPhi = loop[idxPhi-1]
            phi = loop[idxPhi]
            nxGraph.remove_edge(driverPhi, phi)
            CDFG.remove_edge(driverPhi, phi)
            newPO = "n" + driverPhi + "_po"
            CDFG.add_node(newPO, shape="box")
            additionalPOs[newPO] = getWidth(phi, module)
            CDFG.add_edge(driverPhi, newPO, color="red")
            newPI = phi + "_pi"
            CDFG.add_node(newPI, shape="box")
            additionalPIs[newPI] = getWidth(phi, module)
            CDFG.add_edge(newPI, phi, color="red")
            cip_dependencies.append((newPI, newPO, "II"))
        cycle = nx.simple_cycles(nxGraph)
        if cycle == [] or cycle is None:
            break
        loopsNodes = sorted(cycle)
    return additionalPIs, additionalPOs

# function to add phis enable in the PIs
def addPhisEnable(CDFG: pgv.AGraph, module: Module, cip_dependencies: list):

    additionalPIs = {}
    additionalPOs = {}
    nodes = CDFG.nodes()
    for node in nodes:
        if "PHI" in CDFG.get_node(node).attr["label"]:
            srcEnable = None
            assert len(CDFG.in_edges(node)) > 1, "PHI node should have at least 2 inputs"
            for src, dst in CDFG.in_edges(node):
                if CDFG.get_edge(src, dst).attr["style"] == "dashed" and CDFG.get_edge(src, dst).attr["color"] == "red":
                    assert srcEnable is None, "Enable already found"
                    srcEnable = src
            if srcEnable is None:
                srcEnable = node + "_enable"
                additionalPIs[srcEnable] = 1
                CDFG.add_node(srcEnable, shape="box")
                CDFG.add_edge(srcEnable, node, color="red", style="dashed")
            else:
                assert CDFG.get_edge(srcEnable, node).attr["color"] == "red" and CDFG.get_edge(srcEnable, node).attr["style"] == "dashed", "Not correct enable"
                ctrlOut = "n" + srcEnable + "_ctrlOut"
                additionalPOs[ctrlOut] = 1
                CDFG.add_node(ctrlOut, shape="box")
                CDFG.add_edge(srcEnable, ctrlOut, color="red", style="dashed")
                newSrcEnable = node + "_enable"
                additionalPIs[newSrcEnable] = 1
                CDFG.add_node(newSrcEnable, shape="box")
                CDFG.add_edge(newSrcEnable, node, color="red", style="dashed")
                CDFG.remove_edge(srcEnable, node)
                cip_dependencies.append((newSrcEnable, ctrlOut, 0))

    return additionalPIs, additionalPOs  

# function to invert source and destination in cip_dependencies if there is II in the latency
def invertII_Constraints(cip_dependencies: list):
    cip_dependencies_copy = cip_dependencies.copy()
    for dst, src, delay in cip_dependencies_copy:
        if isinstance(delay, str) and "II" in delay:
            cip_dependencies.remove((dst, src, delay))
            cip_dependencies.append((src, dst, delay))

# function to generate the verilog that represents the CDFG
def CDFGToVerilog(_CDFG: pgv.AGraph, module: Module, verilogFilePath: str, jsonFilePath: str, memory_keywords: dict):
    
    CDFG = _CDFG.copy()

    dip_dependencies = {}
    cip_dependencies = []

    # find the memory regex that matches the memory ports
    memoryIdx = None
    memoryReg = memory_keywords["regex_memory"]
    for node in module.getPorts():
        for _memoryIdx in range(len(memoryReg)):
            if re.match(memoryReg[_memoryIdx], node):
                memoryIdx = _memoryIdx
                break
    assert memoryIdx is not None, "Memory regex not found"

    PIs = getPIs(CDFG, module)
    POs = getPOs(CDFG, module)

    phisPIs, cltrOuts = addPhisEnable(CDFG, module, cip_dependencies)
    PIs.update(phisPIs)
    POs.update(cltrOuts)

    additionalPIs, additionalPOs = breakLoopsPhis(CDFG, module, cip_dependencies)
    PIs.update(additionalPIs)
    POs.update(additionalPOs)

    memoryPIs, memoryPOs = addMemoryUnitsPorts(CDFG, module, memory_keywords, memoryIdx, cip_dependencies)
    PIs.update(memoryPIs)
    POs.update(memoryPOs)
    
    multilatencyPIs, multilatencyPOs = addMultiLatencyPorts(CDFG, module, cip_dependencies)
    PIs.update(multilatencyPIs)
    POs.update(multilatencyPOs)


    variables = extractVariables(CDFG, module, PIs.keys(), POs.keys())

    verilogData = ""
    verilogData += generateHeader(list(PIs.keys())+list(POs.keys()))
    verilogData += generateVariablesDef(PIs, POs, variables, dip_dependencies)

    verilogData += generateAssigns(CDFG, module)

    with open(verilogFilePath, "w") as f:
        f.write(verilogData)
        f.write("endmodule\n")

    # the order is inverted since leap backend uses the formulation dst - src >= D where (dst, src, D) is in cip_dependencies
    invertII_Constraints(cip_dependencies)

    finalDataJSON = {"dip": dip_dependencies, "cip": cip_dependencies}

    with open(jsonFilePath, "w") as f:
        json.dump(finalDataJSON, f)
    
    CDFG.write("CDFG_final.dot")
        
