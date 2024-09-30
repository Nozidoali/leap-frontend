import pygraphviz as pgv
from typing import List, Dict
from enum import Enum
from ...modules import *


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
        self.frame: Frame = None

        # Set the "dirty" label for the range
        self._nodeToRange: Dict[str, Range] = {}

    def toBNode(self, node: pgv.Node) -> BNode:
        # TODO: range is not being set
        opName = node.attr["operation"]
        opType = getOpType(opName) if opName != "None" else None
        return OPNode(node.attr["variable_name"], opType, [])

    def toPort(self, node: pgv.Node) -> Port:
        port = self.frame.getPort(self.toBNode(node).name)
        portRange = self.toRange(node)
        port.setRange(portRange)
        return port

    def toRange(self, node: pgv.Node) -> Range:
        if self.getRange(node) is not None:
            return self.getRange(node)
        try:
            width: int = int(node.attr["range"])
            return BasicRange(width)
        except:
            return None

    def toOpType(self, node: pgv.Node) -> OPType:
        return getOpType(node.attr["operation"])

    def setRange(self, node: pgv.Node, range: Range) -> None:
        node = node if isinstance(node, pgv.Node) else self.get_node(node)
        self._nodeToRange[node] = range

    def getRange(self, node: pgv.Node) -> Range:
        node = node if isinstance(node, pgv.Node) else self.get_node(node)
        return self._nodeToRange.get(node, None)

    def add_node(self, node: OPNode, **kwargs) -> str:
        # TODO: convert these to strings and retrieve them in the graph
        kwargs["variable_name"] = node.variable_name
        kwargs["operation"] = node.operation.value

        # TODO: range is not being set
        variable_name = node.variable_name
        if self.frame is None or variable_name not in self.frame.getPortNames():
            portRange = None
        else:
            portRange = self.frame.getPort(variable_name).getRange()

        if portRange is not None:
            kwargs["range"] = portRange.toWidth()
        if node.isVariable() or node.isConstant():
            nodeId = node.toString()
            kwargs["label"] = node.toString()
            kwargs["shape"] = "box"
        else:
            nodeId = str(self.number_of_nodes())  # Use number of nodes as unique ID
            kwargs["label"] = node.name
            kwargs["shape"] = "ellipse"
        super().add_node(nodeId, **kwargs)
        return nodeId

    def addVarNode(self, variable_name: str, range: Range = None) -> str:
        node = VarNode(variable_name)
        # add the range to the frame
        nodeId = self.add_node(node)
        self.setRange(nodeId, range)
        return nodeId

    def addOpNode(
        self, variable_name: str, operation: OPType, children: List[str]
    ) -> str:
        node = OPNode(variable_name, operation, [])
        nodeId = self.add_node(node)
        for childId in children:
            self.add_edge(childId, nodeId)
        return nodeId

    def addAssignment(
        self,
        target: str,
        expression: str,
        condition: str = None,
        event: str = None,
        isBlocking: bool = True,
    ) -> None:
        targetNode = self.get_node(target)
        expressionNode = self.get_node(expression)
        conditionNode = self.get_node(condition) if condition is not None else None
        eventNode = self.get_node(event) if event is not None else None
        self.addEdge(
            expressionNode,
            targetNode,
            eType=EdgeType.VALUE,
            eIndex=self.number_of_edges(),
        )
        if conditionNode is not None:
            self.addEdge(
                conditionNode,
                targetNode,
                eType=EdgeType.CONDITION,
                eIndex=self.number_of_edges(),
            )
        if eventNode is not None:
            self.addEdge(
                eventNode,
                targetNode,
                eType=EdgeType.EVENT,
                eIndex=self.number_of_edges(),
            )

        # Set the assignment attributes on the lhs node
        targetNode.attr["isBlocking"] = isBlocking

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
        self, source: pgv.Node, target: pgv.Node, eIndex: int, eType: EdgeType
    ) -> None:
        eType = eType.value if isinstance(eType, EdgeType) else eType
        edge_attrs = {
            "eType": eType,
            "eIndex": eIndex,
            "xlabel": f"{eType}_{eIndex}",
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

    # we need to override the add_edge method to maintain the child order
    def add_edge(self, u, v=None, key=None, **attr):
        # pred id is the number of predecessors of the target node
        predId = len(self.predecessors(v))
        attr["predId"] = predId
        return super().add_edge(u, v, key, **attr)

    # override the predecessors method to sort the predecessors based on predId
    def predecessors(self, n):
        preds = super().predecessors(n)
        return sorted(preds, key=lambda x: self.get_edge(x, n).attr["predId"])

    @staticmethod
    def toNode(node: pgv.Node) -> BNode:
        opName = node.attr["operation"]
        opType = getOpType(opName) if opName != "None" else None
        return OPNode(node.attr["variable_name"], opType, [])

    @property
    def variables(self) -> List[str]:
        return [node for node in self.nodes() if CDFGraph.toNode(node).isVariable()]

    @property
    def pis(self) -> List[pgv.Node]:
        return [
            node
            for node in self.variables
            if len(self.predecessors(node)) == 0 and len(self.successors(node)) > 0
        ]

    @property
    def pos(self) -> List[pgv.Node]:
        return [
            node
            for node in self.variables
            if len(self.predecessors(node)) > 0 and len(self.successors(node)) == 0
        ]

    @property
    def internalNodes(self) -> List[pgv.Node]:
        return [
            node
            for node in self.variables
            if len(self.predecessors(node)) > 0 and len(self.successors(node)) > 0
        ]

    @staticmethod
    def isCond(edge: pgv.Edge) -> bool:
        return edge.attr["eType"] == EdgeType.CONDITION.value

    @staticmethod
    def isEvent(edge: pgv.Edge) -> bool:
        return edge.attr["eType"] == EdgeType.EVENT.value


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


def _detectFrame(graph: CDFGraph) -> Frame:
    frame = Frame()
    frame.addPorts(
        [OutputPort(CDFGraph.toNode(x), graph.toRange(x)) for x in graph.pos]
    )
    frame.addPorts([InputPort(CDFGraph.toNode(x), graph.toRange(x)) for x in graph.pis])
    frame.addPorts(
        [BasicPort(CDFGraph.toNode(x), graph.toRange(x)) for x in graph.internalNodes]
    )
    return frame


def hasLoop(graph: CDFGraph) -> bool:

    def _hasLoop(node: pgv.Node, visited: set) -> bool:
        if node in visited:
            return True
        visited.add(node)
        for child in graph.predecessors(node):
            if _hasLoop(child, visited):
                return True
        visited.remove(node)
        return False

    visited = set()
    for node in graph.nodes():
        if node not in visited:
            if _hasLoop(node, visited):
                return True
    return False


def graphToModule(graph: CDFGraph, param: dict = {}) -> Module:
    """
    WARNING: This function only works for trees, not for graphs with cycles.
    """
    if hasLoop(graph):
        raise Exception("Cannot convert a graph with loops to a module")

    module = Module()  # Initialize a new Module
    graph.frame = graph.frame or _detectFrame(graph)

    # for debug
    # print("Variables: ", graph.variables)
    # print("PIs: ", graph.pis)
    # print("POs: ", graph.pos)
    # print("Internal Nodes: ", graph.internalNodes)

    # Iterate over all nodes in the graph and recreate DFGNodes
    for node in graph.nodes():
        if node in graph.variables:
            port: Port = graph.toPort(node)
            range: Range = graph.toRange(node)
            port.setRange(range)
            module.addPort(port)

            # get assignments
            for val, cond, event in graph.getAssignments(node):
                target = CDFGraph.toNode(node)
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
            new_node_id = new_graph.add_node(CDFGraph.toNode(node), **node.attr)
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
            new_node_id = new_graph.add_node(CDFGraph.toNode(node), **node.attr)
            operation_to_nodes[operation][children_signatures] = new_node_id
            old_to_new_node[node] = new_node_id
            return new_node_id

    # Create a new graph
    new_graph = CDFGraph()
    new_graph.frame = graph.frame.copy()

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


def extractWindow(
    graph: CDFGraph, node: pgv.Node, cut: List[pgv.Node] = []
) -> CDFGraph:
    """
    Extract a window around a specific node in the graph.
    """

    def _extract_node(root: pgv.Node, old_to_new_node: set) -> str:
        """
        Recursively extract a node and its predecessors.
        """
        if root in old_to_new_node:
            return old_to_new_node[root]

        # create a new node in the new graph
        new_node_id = new_graph.add_node(CDFGraph.toNode(root), **root.attr)
        old_to_new_node[root] = new_node_id

        for child in graph.predecessors(root):
            if CDFGraph.isCond(graph.get_edge(child, root)):
                return new_node_id

        for child in graph.predecessors(root):
            if CDFGraph.isEvent(graph.get_edge(child, root)):
                continue
            child_id = _extract_node(child, old_to_new_node)
            new_graph.add_edge(
                child_id, new_node_id, **graph.get_edge(child, root).attr
            )

        return new_node_id

    # Create a new graph
    new_graph = CDFGraph()

    # Extract the window around the specified node
    old_to_new_node: Dict[pgv.Node, str] = {}

    # Add the cut nodes to the new graph
    cut: List[pgv.Node] = [
        x if isinstance(x, pgv.Node) else graph.get_node(x) for x in cut
    ]
    for leaf in cut:
        leaf_id = new_graph.add_node(CDFGraph.toNode(leaf), **leaf.attr)
        old_to_new_node[leaf] = leaf_id

    node = node if isinstance(node, pgv.Node) else graph.get_node(node)
    _extract_node(node, old_to_new_node)

    return new_graph


def elaborateConditionsAt(graph: CDFGraph, node: pgv.Node) -> None:

    node: pgv.Node = node if isinstance(node, pgv.Node) else graph.get_node(node)
    id2assignment: Dict[int, Dict[EdgeType, pgv.Node]] = {}

    for predecessor in graph.predecessors(node):
        edge: pgv.Edge = graph.get_edge(predecessor, node)

        # Get index and edge type from edge attributes
        idx: int = int(edge.attr["eIndex"])
        eType: EdgeType = EdgeType(edge.attr["eType"])

        # Initialize the assignment dict for this index if not already done
        if idx not in id2assignment:
            id2assignment[idx] = {eType: None for eType in EdgeType}

        # Assign the predecessor node to the correct edge type in the assignment
        id2assignment[idx][eType] = predecessor

    # change the condition to a MUX node if there are multiple conditions
    if len(id2assignment) <= 1:
        return

    # get the default value
    defaultValNode = None
    for idx, assignment in id2assignment.items():
        condNode = assignment[EdgeType.CONDITION]
        valNode = assignment[EdgeType.VALUE]
        if condNode is None:
            assert defaultValNode is None, "Multiple default values found"
            defaultValNode = valNode

    currHeadNode: pgv.Node = defaultValNode or graph.get_node(
        graph.add_node(ConstantNode("0"))
    )
    assert isinstance(currHeadNode, pgv.Node)
    for idx, assignment in id2assignment.items():
        condNode = assignment[EdgeType.CONDITION]
        valNode = assignment[EdgeType.VALUE]

        if condNode is None:
            continue

        # create a new MUX node
        muxNode = OPNode(
            f"?:",
            OPType.CONDITIONAL_EXPRESSION,
            CDFGraph.toNode(condNode),
            CDFGraph.toNode(valNode),
            CDFGraph.toNode(currHeadNode),
        )
        muxNodeId = graph.add_node(muxNode)

        for pred in [condNode, valNode, currHeadNode]:
            if pred == condNode:
                graph.add_edge(pred, muxNodeId, color="red")
            else:
                graph.add_edge(pred, muxNodeId)

        currHeadNode = graph.get_node(muxNodeId)

    # remove the previous predecessors of the node
    for pred in list(graph.predecessors(node)):
        graph.delete_edge(pred, node)

    # add the new edge
    graph.addEdge(currHeadNode, node, 0, EdgeType.VALUE)
