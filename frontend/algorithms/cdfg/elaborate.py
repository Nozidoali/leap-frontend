from .cdfg import *
import pygraphviz as pgv
from typing import List, Dict
from ...modules import *


def fullElaborate(graphOld: CDFGraph) -> CDFGraph:
    """
    Fully elaborate the conditions in the graph.
    """

    def _elaborateOperation(
        graph: CDFGraph, operation: OPType, children_ids: List[str], maxWidth: int
    ) -> List[str]:
        # TODO: implement this function
        root_ids: List[str] = []
        match operation:
            case OPType.BINARY_LT | OPType.BINARY_GT:
                width: int = max((len(x) for x in children_ids))
                child_id1: List[str] = children_ids[0]
                child_id2: List[str] = children_ids[1]
                root_id: str = None
                for i in range(min(width, maxWidth)):
                    new_node_id: str = graph.add_node(OPNode("<", OPType.BINARY_LT))
                    graph.add_edge(child_id1[i], new_node_id)
                    graph.add_edge(child_id2[i], new_node_id)
                    if root_id:
                        new_node_id2 = graph.add_node(OPNode("&", OPType.BINARY_AND))
                        graph.add_edge(root_id, new_node_id2)
                        graph.add_edge(new_node_id, new_node_id2)
                        root_id = new_node_id2
                    else:
                        root_id = new_node_id
                root_ids.append(root_id)
            case OPType.UNARY_NOT:
                width: int = len(children_ids[0])
                child_id: List[str] = children_ids[0]
                for i in range(min(width, maxWidth)):
                    new_node_id: str = graph.add_node(OPNode("!", OPType.UNARY_NOT))
                    graph.add_edge(child_id[i], new_node_id)
                    root_ids.append(new_node_id)
            case OPType.CONDITIONAL_EXPRESSION:
                width: int = max((len(x) for x in children_ids[1:]))
                cond_id: List[str] = children_ids[0]
                true_id: List[str] = children_ids[1] + [
                    graph.add_node(ConstantNode("0"))
                    for _ in range(width - len(children_ids[1]))
                ]
                false_id: List[str] = children_ids[2] + [
                    graph.add_node(ConstantNode("0"))
                    for _ in range(width - len(children_ids[2]))
                ]
                for i in range(min(width, maxWidth)):
                    new_node_id: str = graph.add_node(OPNode("?:", operation))
                    graph.add_edge(cond_id[0], new_node_id)
                    graph.add_edge(true_id[i], new_node_id)
                    graph.add_edge(false_id[i], new_node_id)
                    root_ids.append(new_node_id)
            case OPType.BINARY_AND | OPType.BINARY_OR:
                width: int = max((len(x) for x in children_ids))
                for i in range(min(width, maxWidth)):
                    new_node_id: str = graph.add_node(OPNode("&&", OPType.BINARY_AND))
                    for child_id in children_ids:
                        graph.add_edge(child_id[i], new_node_id)
                    root_ids.append(new_node_id)

            case _:
                raise NotImplementedError(f"Operation {operation} is not implemented")

        return root_ids

    def _elaborateNode(
        _graphOld: CDFGraph,
        _graphNew: CDFGraph,
        node: pgv.Node,
        old_to_new_node: Dict[pgv.Node, str],
        maxWidth: int,
    ) -> List[str]:
        """
        Recursively elaborate the conditions in the graph.
        """
        if node in old_to_new_node:
            return old_to_new_node[node]

        if CDFGraph.toNode(node).isVariable() or CDFGraph.toNode(node).isConstant():
            # create a set of new nodes based on the old node's range
            nodeRange = _graphOld.toRange(node) or BasicRange(1)
            width = nodeRange.toWidth()

            if CDFGraph.toNode(node).isConstant():
                new_node_id = _graphNew.add_node(
                    ConstantNode(f"{node.attr['variable_name']}"), **node.attr
                )
                new_node_ids = [new_node_id for i in range(width)]
            else:
                root_node_id = _graphNew.add_node(
                    VarNode(f"{node.attr['variable_name']}", nodeRange), **node.attr
                )
                # create a new node for each bit in the range
                new_node_ids = []
                for i in range(width):
                    index_node_id = _graphNew.add_node(ConstantNode(i), **node.attr)
                    new_node_id = _graphNew.add_node(
                        OPNode("[]", OPType.ARRAY_INDEX), **node.attr
                    )
                    _graphNew.add_edge(root_node_id, new_node_id)
                    _graphNew.add_edge(index_node_id, new_node_id)
                    new_node_ids.append(new_node_id)
            old_to_new_node[node] = new_node_ids
            return new_node_ids

        # now its an operation node
        children_ids = []
        for child in _graphOld.predecessors(node):
            children_ids.append(
                _elaborateNode(_graphOld, _graphNew, child, old_to_new_node, maxWidth)
            )
        operation = _graphOld.toOpType(node)
        root_ids = _elaborateOperation(_graphNew, operation, children_ids, maxWidth)

        return root_ids

    # Create a new graph
    graphNew = CDFGraph()

    # Elaborate the conditions in the graph
    old_to_new_node: Dict[pgv.Node, str] = {}

    # Elaborate all nodes in the graph
    for node in graphOld.pos:
        nodeRange = graphOld.toRange(node) or BasicRange(1)
        width: int = nodeRange.toWidth()
        assert len(graphOld.predecessors(node)) == 1
        expression = graphOld.predecessors(node)[0]
        # print(f"width = {width}")
        root_ids = _elaborateNode(
            graphOld, graphNew, expression, old_to_new_node, maxWidth=width
        )

        node_id = graphNew.add_node(CDFGraph.toNode(node), **node.attr)
        for root_id in root_ids:
            graphNew.addEdge(
                root_id, node_id, graphNew.number_of_edges(), EdgeType.VALUE
            )

    return graphNew
