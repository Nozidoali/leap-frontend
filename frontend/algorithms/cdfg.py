import pygraphviz as pgv
from typing import List, Tuple, Dict
from enum import Enum
from ..modules import *


class EdgeType(Enum):
    VALUE = "val"
    CONDITION = "cond"
    EVENT = "event"


class CDFGraph(pgv.AGraph):

    def __init__(self, strict: bool = False, directed: bool = True, **kwargs):
        # Initialize the AGraph with the required arguments
        super().__init__(strict=strict, directed=directed, **kwargs)

        # Custom properties for CDFGraph
        self.nodeToAssignment = {}
        self.frame: Frame = None

    def add_node(self, node: DFGNode, **kwargs) -> str:
        # TODO: convert these to strings and retrieve them in the graph
        kwargs["variable_name"] = node.variable_name
        kwargs["operation"] = node.operation.value
        kwargs["range"] = node.range
        if node.isVariable():
            nodeId = node.toString()
            kwargs["label"] = node.toString()
            kwargs["shape"] = "box"
        else:
            nodeId = str(self.number_of_nodes())  # Use number of nodes as unique ID
            kwargs["label"] = node.name
            kwargs["shape"] = "ellipse"
        super().add_node(nodeId, **kwargs)
        return nodeId

    def isVariable(self, node: pgv.Node) -> bool:
        return node.attr["operation"] == "VARIABLE"

    def getAssignments(self, node: pgv.Node) -> List[Dict[EdgeType, pgv.Node]]:
        # for each predecessor of the node, check the edge and get the assignment
        id2assignment: Dict[int, Dict[EdgeType, pgv.Node]] = {}
        for predecessor in self.predecessors(node):
            edge = self.get_edge(predecessor, node)

            # we check the condition and value of the edge
            idx: int = edge.attr["eIndex"]
            eType: EdgeType = edge.attr["eType"]

            if idx not in id2assignment:
                id2assignment[idx] = {
                    EdgeType.VALUE.value: None,
                    EdgeType.CONDITION.value: None,
                    EdgeType.EVENT.value: None,
                }
            id2assignment[idx][eType] = predecessor
        # Create a list of assignments, based on sorted index
        return [
            (
                id2assignment[idx][EdgeType.VALUE.value],
                id2assignment[idx][EdgeType.CONDITION.value],
                id2assignment[idx][EdgeType.EVENT.value],
            )
            for idx in sorted(id2assignment.keys())
        ]

    def add_value_edge(self, source: pgv.Node, target: pgv.Node, idx: int) -> None:
        self.add_edge(
            source, target, xlabel=f"val_{idx}", eType=EdgeType.VALUE.value, eIndex=idx
        )

    def add_condition_edge(self, source: pgv.Node, target: pgv.Node, idx: int) -> None:
        self.add_edge(
            source,
            target,
            style="dashed",
            color="red",
            xlabel=f"cond_{idx}",
            eType=EdgeType.CONDITION.value,
            eIndex=idx,
        )

    def add_event_edge(self, source: pgv.Node, target: pgv.Node, idx: int) -> None:
        self.add_edge(
            source,
            target,
            style="dotted",
            color="blue",
            xlabel=f"event_{idx}",
            eType=EdgeType.EVENT.value,
            eIndex=idx,
        )

    @staticmethod
    def toNode(node: pgv.Node) -> DFGNode:
        opName = node.attr["operation"]
        opType = getOpType(opName) if opName != "None" else None
        return OPNode(node.attr["variable_name"], opType, [])


# External function to recursively add a DFGNode to the graph
def _addNodeRecursively(graph: CDFGraph, node: DFGNode) -> str:
    nodeId = graph.add_node(node)
    # Recursively add children nodes and edges
    for child in node.children:
        childId = _addNodeRecursively(graph, child)
        graph.add_edge(childId, nodeId)

    return nodeId


# External function to create a CDFGraph from a Module
def moduleToGraph(module: Module) -> CDFGraph:
    # Initialize the graph
    graph = CDFGraph()

    # Set the port frame
    graph.frame = module.getFrame()

    # Loop through the module assignments and add them to the graph
    for i, assignment in enumerate(module.assignments):

        # Process the lhs (target) and rhs (expression)
        lhsNode = _addNodeRecursively(graph, assignment.target)
        rhsNode = _addNodeRecursively(graph, assignment.expression)

        # Add the event edge
        if assignment.event is not None:
            eventNode = _addNodeRecursively(graph, assignment.event)
            graph.add_event_edge(eventNode, lhsNode, i)

        # Add the assignment edge
        graph.add_value_edge(rhsNode, lhsNode, i)
        if assignment.condition is not None:
            conditionNode = _addNodeRecursively(graph, assignment.condition)
            graph.add_condition_edge(conditionNode, lhsNode, i)

        # Set the assignment attributes on the lhs node
        lhs = graph.get_node(lhsNode)
        lhs.attr["isBlocking"] = assignment.isBlocking

    return graph


def graphToModule(graph: CDFGraph, param: dict = {}) -> Module:
    module = Module()  # Initialize a new Module
    autoDerivePortDirection = param.get("autoDerivePortDirection", True)

    # Iterate over all nodes in the graph and recreate DFGNodes
    for node in graph.nodes():
        if node in graph.frame.getPortNames():
            port: Port = graph.frame.getPort(node)

            if autoDerivePortDirection:
                # if the node has no children, it is a input port
                if len(graph.successors(node)) == 0:
                    port.setDirection(PortDirection.INPUT, override=True)
                # if the node has no parents, it is a output port
                elif len(graph.predecessors(node)) == 0:
                    port.setDirection(PortDirection.OUTPUT, override=True)
                # else it is a internal signal
                else:
                    port.setDirection(None, override=True)

            module.addPort(port)

            # get assignments
            for val, cond, event in graph.getAssignments(node):
                target = VarNode(node)
                expression = _recreateDFGNode(graph, val)
                condition = _recreateDFGNode(graph, cond) if cond is not None else None
                event = _recreateDFGNode(graph, event) if event is not None else None
                assignment = Assignment(
                    target,
                    expression,
                    condition,
                    event,
                    node.attr.get("isBlocking", True),
                )
                module.addAssignment(assignment)

    return module


def _recreateDFGNode(graph: CDFGraph, node: pgv.Node) -> DFGNode:
    """
    Recreate a DFGNode based on its ID in the graph.
    """
    # Rebuild the node based on its shape and attributes in the graph
    assert isinstance(node, pgv.Node)
    newNode = CDFGraph.toNode(node)
    children = []
    for childId in graph.predecessors(node):
        childNode = _recreateDFGNode(graph, childId)
        children.append(childNode)
    newNode.children = children
    return newNode
