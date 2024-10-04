from ..modules import *
from .highlight import *
import pygraphviz as pgv
from collections import deque
import re

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
                        dataEndPoint = "finish"
                    else:
                        assert False, "Data end point associate to ctrl node not found"
                    if pipelineGraph is not None and driverCtrl in pipelineGraph.nodes():
                        if driverCtrl in pipelineGraph.nodes():
                            if not driverCtrl in departureStates.keys():
                                departureStates[driverCtrl] = []
                            departureStates[driverCtrl].append(dataEndPoint)
                        else:
                            departureStates[state].append(dataEndPoint)
                    else:
                        departureStates[state].append(dataEndPoint)

    insertPipelineGraphs(graph, FSM , pipelineGraphs)

    return departureStates

# function to get the memory operations associated with a state
def getStatesMem(module: Module, enablePort: str, state2node: dict):
    assert module.isDefined(enablePort), "Output address port not found"
    numOps = 0
    statesMem = []
    for assign in module.getAssignmentsOf(enablePort):
        assert assign.expression.isConstant(), "Enable port is not a constant"
        value = assign.expression.toString()
        if value == "1'b0" or value == "0" or value == "1'd0":
            continue
        numOps += 1
        # TODO: find general solution for finding right state
        target, expression, condition = getAssignToNode(module, assign)
        foundState = None
        for state in state2node.keys():
            if enablePort in state2node[state]:
                foundState = state
                break
        assert foundState is not None, "State not found"
        statesMem.append(foundState)
    if numOps == 0:
        return None
    return statesMem

# function to get memory operation types associated with a state
def getMemOpState(module: Module, writeEnablePort: str, state2node: dict):
    assert module.isDefined(writeEnablePort), "Write enable port not found"
    stateToOp = {}
    for assign in module.getAssignmentsOf(writeEnablePort):
        assert assign.expression.isConstant(), "Write enable port is not a constant"
        value = assign.expression.toString()
        if value == "1'b0" or value == "0" or value == "1'd0":
            continue
        foundState = None
        # TODO: find general solution for finding right state
        for state in state2node.keys():
            if writeEnablePort in state2node[state]:
                foundState = state
                break
        assert foundState is not None, "State not found"
        stateToOp[foundState] = value
    return stateToOp

# function to merge memory ports of the CDFG
def memory_merge(module: Module, CDFG: pgv.AGraph, state2node: dict, memory_keywords: dict):

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
    print(memories)
    assert len(memories) > 0, "No memory ports found"
    for memory_name in memories.keys():
        for memory_id in memories[memory_name]:
            memoryNodes = {}
            for node in CDFG.nodes():
                for keyword in memory_keywords.keys():
                    memoryNode = memory_keywords[keyword][0].replace("MEMORY_NAME", memory_name).replace("MEMORY_ID", memory_id)
                    if memoryNode == node.get_name():
                        assert keyword not in memoryNodes.keys(), "Memory node already exists"
                        memoryNodes[keyword] = node
            # assert that memory nodes and memory keywords have the same length apart from the regex
            assert len(memoryNodes) < len(memory_keywords) - 2, "Memory nodes not found"
            statesMem = getStatesMem(module, memoryNodes["enable"], state2node)
            if statesMem is None:
                continue
            stateToOp = getMemOpState(module, memoryNodes["writeEnable"], state2node)

    # remove the nodes still existing in the CDFG and all the nodes connected to them

# function to merge consecutive pipeline states
def mergeConsecutivePipelineStates(FSM: pgv.AGraph, departureStates: dict, arrivalStates: list):

    mergedStates = {}
    for edge in FSM.edges():
        if "info" in FSM.get_edge(edge[0], edge[1]).attr.keys():
            info = FSM.get_edge(edge[0], edge[1]).attr["info"]
            if "NumRegs" in info:
                numRegs = int(info.split("=")[1])
                if numRegs == 0:
                    mergedStates[edge[0]] = edge[1] 
    for src, dst in mergedStates.items():
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
        copy_arrival = arrivalStates.copy()
        for dataSrcNode, arrivalState in copy_arrival:
            if arrivalState == dst:
                arrivalStates.remove((dataSrcNode, arrivalState))
                arrivalStates.append((dataSrcNode, src))

    FSM.write("FSM_merged.dot")

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
    departureStates = getDepartureStates(graph, outCtrlInDataWire, module, FSM, end_nodes)
    arrivalStates = getArrivalStates(graph, inCtrlOutDataWire, module, end_nodes, FSM)
    for dataSrcNode, arrivalState in arrivalStates:
        assert arrivalState in departureStates.keys(), "Arrival state not found"
        dataDstNodes = departureStates[arrivalState]
        for dataDstNode in dataDstNodes:
            CDFG.add_edge(dataSrcNode.get_name(), dataDstNode, color="red", style="dashed")
        #print(f"Data node {dataSrcNode.get_name()} -> {dataDstNodes}")
    # the pipeline states with no registers across them should be merged since do not represent real states
    mergeConsecutivePipelineStates(FSM, departureStates, arrivalStates)
    memory_merge(module, CDFG, departureStates, memory_keywords)

    return CDFG
