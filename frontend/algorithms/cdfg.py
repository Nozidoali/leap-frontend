import pygraphviz as pgv
from typing import List, Dict
from enum import Enum
from ..modules import *


class EdgeType(Enum):
    VALUE = "val"
    CONDITION = "cond"
    EVENT = "event"


class CDFGraph(pgv.AGraph):

    def __init__(self, strict: bool = False, directed: bool = True, **kwargs):
        # Initialize the AGraph with the required arguments
        super().__init__(
            strict=strict, directed=directed, splines="ortho", rankdir="TB", **kwargs
        )

        # Custom properties for CDFGraph
        self.nodeToAssignment = {}
        self.frame: Frame = None

    def toBNode(self, node: pgv.Node) -> BNode:
        # TODO: range is not being set
        opName = node.attr["operation"]
        opType = getOpType(opName) if opName != "None" else None
        return OPNode(node.attr["variable_name"], opType, [])

    def add_node(self, node: OPNode, **kwargs) -> str:
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

    def getAssignments(self, node: pgv.Node) -> List[Dict[EdgeType, pgv.Node]]:
        """
        Retrieves assignments for a given node based on its incoming edges.
        """
        id2assignment: Dict[int, Dict[EdgeType, pgv.Node]] = {}

        for predecessor in self.predecessors(node):
            edge = self.get_edge(predecessor, node)

            # Get index and edge type from edge attributes
            idx: int = int(edge.attr["eIndex"])
            eType: EdgeType = EdgeType(edge.attr["eType"])

            # Initialize the assignment dict for this index if not already done
            if idx not in id2assignment:
                id2assignment[idx] = {eType: None for eType in EdgeType}

            # Assign the predecessor node to the correct edge type in the assignment
            id2assignment[idx][eType] = predecessor

        # Create a list of assignments, based on sorted index
        return [
            tuple(
                id2assignment[idx][eType] for eType in EdgeType
            )  # Iterate over EdgeType
            for idx in sorted(id2assignment.keys())
        ]

    def addEdge(
        self, source: pgv.Node, target: pgv.Node, idx: int, eType: EdgeType
    ) -> None:
        eType = eType.value if isinstance(eType, EdgeType) else eType
        edge_attrs = {
            "eType": eType,
            "eIndex": idx,
            "xlabel": f"{eType}_{idx}",
        }
        # Customize edge styles based on the edge type
        if eType == EdgeType.CONDITION.value:
            edge_attrs.update({"style": "dashed", "color": "red"})
        elif eType == EdgeType.EVENT.value:
            edge_attrs.update({"style": "dotted", "color": "blue"})
        else:
            edge_attrs.update({"style": "solid", "color": "black"})
        # Add the edge with the specified attributes
        self.add_edge(source, target, **edge_attrs)

    @staticmethod
    def toNode(node: pgv.Node) -> BNode:
        opName = node.attr["operation"]
        opType = getOpType(opName) if opName != "None" else None
        return OPNode(node.attr["variable_name"], opType, [])


# External function to recursively add a BNode to the graph
def _addNodeRecursively(graph: CDFGraph, node: BNode) -> str:
    nodeId = graph.add_node(node)
    # Recursively add children nodes and edges
    for child in node.children:
        assert isinstance(child, BNode)
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
            graph.addEdge(eventNode, lhsNode, i, EdgeType.EVENT)

        # Add the assignment edge
        graph.addEdge(rhsNode, lhsNode, i, EdgeType.VALUE)
        if assignment.condition is not None:
            conditionNode = _addNodeRecursively(graph, assignment.condition)
            graph.addEdge(conditionNode, lhsNode, i, EdgeType.CONDITION)

        # Set the assignment attributes on the lhs node
        lhs = graph.get_node(lhsNode)
        lhs.attr["isBlocking"] = assignment.isBlocking

    return graph


def _detectPortDirection(graph: CDFGraph, node: pgv.Node) -> PortDirection:
    if len(graph.successors(node)) == 0:
        return PortDirection.INPUT
    elif len(graph.predecessors(node)) == 0:
        return PortDirection.OUTPUT
    return None


def graphToModule(graph: CDFGraph, param: dict = {}) -> Module:
    module = Module()  # Initialize a new Module
    autoDerivePortDirection = param.get("autoDerivePortDirection", True)

    # Iterate over all nodes in the graph and recreate DFGNodes
    for node in graph.nodes():
        if node in graph.frame.getPortNames():
            port: Port = graph.frame.getPort(node)

            if autoDerivePortDirection:
                port.direction = _detectPortDirection(graph, node)
            module.addPort(port)

            # get assignments
            for val, cond, event in graph.getAssignments(node):
                target = VarNode(str(node))
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


def _recreateDFGNode(graph: CDFGraph, node: pgv.Node) -> BNode:
    """
    Recreate a BNode based on its ID in the graph.
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


def reduce(graph: CDFGraph) -> CDFGraph:
    """
    Run structural hashing on the graph and merge nodes with the same functionality and the same children.
    """

    def _reduce_node(
        node: pgv.Node,
        old_to_new_node: Dict[pgv.Node, str],
        operation_to_nodes: Dict[str, Dict[tuple, str]],
    ) -> str:
        """
        Recursively reduce a node and its predecessors.
        """
        if node in old_to_new_node:
            return old_to_new_node[node]

        if CDFGraph.toNode(node).isVariable() or CDFGraph.toNode(node).isConstant():
            new_node_id = new_graph.add_node(CDFGraph.toNode(node))
            old_to_new_node[node] = new_node_id
            return new_node_id

        operation = node.attr["operation"]
        children_ids = []
        for child in graph.predecessors(node):
            children_ids.append(
                _reduce_node(child, old_to_new_node, operation_to_nodes)
            )
        children_signatures = tuple(children_ids)

        if operation not in operation_to_nodes:
            operation_to_nodes[operation] = {}
        if children_signatures in operation_to_nodes[operation]:
            existing_node = operation_to_nodes[operation][children_signatures]
            old_to_new_node[node] = existing_node
            return existing_node
        else:
            new_node_id = new_graph.add_node(CDFGraph.toNode(node))
            operation_to_nodes[operation][children_signatures] = new_node_id
            old_to_new_node[node] = new_node_id
            return new_node_id

    # Create a new graph
    new_graph = CDFGraph()

    # Dictionary to map old nodes to new nodes in the new graph
    old_to_new_node: Dict[pgv.Node, str] = {}
    operation_to_nodes: Dict[str, Dict[tuple, str]] = {}

    # Reduce all nodes in the graph
    for node in list(graph.nodes()):
        _reduce_node(node, old_to_new_node, operation_to_nodes)
        assert node in old_to_new_node

    # Add edges to the new graph
    edge_exists: Dict[tuple, bool] = {}
    for edge in graph.edges():
        source = old_to_new_node[edge[0]]
        target = old_to_new_node[edge[1]]

        edge_signature = (source, target)
        if edge_signature in edge_exists:
            continue
        edge_exists[edge_signature] = True

        edge_attrs = graph.get_edge(edge[0], edge[1]).attr
        new_graph.add_edge(source, target, **edge_attrs)

    return new_graph
