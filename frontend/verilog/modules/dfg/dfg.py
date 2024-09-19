#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 12:23:16
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 12:55:05
"""

from .unit import *


class DFGraph:
    class Node:
        def __init__(self, node: int) -> None:
            self.node = node
            self.op = None
            self.range = None
            self.label: str = None
            self.children = []
            self.parents = []

        def __repr__(self) -> str:
            return f"{self.node.variable_name} -> {self.children}"

        def getVariableName(self):
            if self.op == SOPType.VARIABLE:
                return self.label
            if self.op == SOPType.CONST:
                return self.label
            return None

        @property
        def isVariable(self):
            return self.op == SOPType.VARIABLE

        @property
        def hasChildren(self):
            return len(self.children) > 0

    def __init__(self) -> None:
        self.nodes = []
        self.__node_index: int = 0
        self.__node_trav_index = 0
        self.__variable_definitions = {}
        self.__variable_fanouts = {}

        self.__nodes = []
        self.__variable_to_node_index = {}
        self.__operation_to_nodes_index = {
            opName: []
            for opName in [op.value for op in SOPType]
            + [op.value for op in AOPType]
            + [op.value for op in BOPType]
            + [op.value for op in UOPType]
        }

    def createNewNode(self):
        curr_index = self.__node_index
        self.__node_index += 1
        return curr_index

    @staticmethod
    def getVariableName(node: DFGNode):
        if node.operation == SOPType.VARIABLE:
            # we need to consider the range
            if node.range is not None:
                return f"{node.variable_name}{node.range}"
            return node.variable_name
        if node.operation == SOPType.CONST:
            return node.variable_name
        return None

    def insertNode(self, node: DFGNode) -> int:
        # topological sort
        children = []
        for child in node.children:
            index = self.insertNode(child)
            children.append(index)
        variableName = self.getVariableName(node)
        if variableName is not None and variableName in self.__variable_to_node_index:
            index = self.__variable_to_node_index[variableName]
            # we expend the children
            self.__nodes[index].children.extend(children)
            return index
        elif variableName is None:
            # only hash non-trivial nodes
            nodesWithSameOp = self.__operation_to_nodes_index[node.operation.value]
            for index in nodesWithSameOp:
                if self.__nodes[index].children == children:
                    return index
        rootIndex = self.createNewNode()
        if variableName is not None:
            self.__variable_to_node_index[variableName] = rootIndex
        self.__operation_to_nodes_index[node.operation.value].append(rootIndex)

        # sanity check
        assert isinstance(
            node.variable_name, str
        ), f"node = {node}, node type = {type(node)}"

        node: DFGNode
        newNode = self.Node(node)
        newNode.children = children
        newNode.op = node.operation
        newNode.label = node.variable_name
        newNode.range = node.range

        for child in children:
            self.__nodes[child].parents.append(rootIndex)
        self.__nodes.append(newNode)
        assert rootIndex == len(self.__nodes) - 1
        return rootIndex

    def extractNodeHelper(self, nodeIdx: int) -> DFGNode:
        node = self.__nodes[nodeIdx]
        if node.op == SOPType.VARIABLE:
            # we need to set the range
            dfgNode = VariableNode(node.label)
            if node.range is not None:
                dfgNode.setRange(node.range)
            return dfgNode
        if node.op == SOPType.CONST:
            return ConstantNode(node.label)
        if isinstance(node.op, BOPType):
            assert len(node.children) == 2
            left = self.extractNodeHelper(node.children[0])
            right = self.extractNodeHelper(node.children[1])
            return BinaryOpNode(node.op, left, right)
        if isinstance(node.op, UOPType):
            assert len(node.children) == 1
            child = self.extractNodeHelper(node.children[0])
            return UnaryOpNode(node.op, child)
        if isinstance(node.op, SOPType):
            if node.op == SOPType.WIRE:
                # we don't need to do anything
                assert len(node.children) == 1
                return self.extractNodeHelper(node.children[0])
            if node.op == SOPType.CONDITIONAL_ASSIGN:
                raise NotImplementedError
            if node.op == SOPType.CONCAT:
                children = [self.extractNodeHelper(child) for child in node.children]
                return ConcatOpNode(children)
            if node.op == SOPType.FUNCTION:
                children = [self.extractNodeHelper(child) for child in node.children]
                return FuncNode(node.label, children)
        print(f"node = {node}, node.op = {node.op}")
        raise NotImplementedError

    def extractNode(self, variableName: str):
        assert isinstance(variableName, str), f"variableName = {variableName}"
        assert (
            variableName in self.__variable_to_node_index
        ), f"variableName = {variableName} not found"
        nodeIdx = self.__variable_to_node_index[variableName]
        return self.extractNodeHelper(nodeIdx)

    def getNodes(self):
        return self.__nodes

    def getNode(self, index: int):
        return self.__nodes[index]

    def toGraph(self, dotFile: str):
        try:
            # raise ImportError
            import pygraphviz as pgv

            graph = pgv.AGraph(directed=True)
            for i, node in enumerate(self.__nodes):
                graph.add_node(i, label=node.label)
                if node.op == SOPType.CONDITIONAL_ASSIGN:
                    graph.add_edge(node.children[0], i, style="dashed")
                    for child in node.children[1:]:
                        graph.add_edge(child, i)
                else:
                    for child in node.children:
                        graph.add_edge(child, i)
            graph.write(dotFile)
        except ImportError or ModuleNotFoundError as e:
            # if pygraphviz is not installed, use pydot
            import pydot

            graph = pydot.Dot(graph_type="digraph")

            # add subgraph
            subgraphFSM = pydot.Cluster("FSM")
            subgraphOther = pydot.Cluster("Other")
            # add nodes
            for i, node in enumerate(self.__nodes):
                for child in node.children:
                    # if the child is an assign, we bypass it
                    if (
                        self.__nodes[child].label == "cur_state"
                        or self.__nodes[child].label == "next_state"
                    ):
                        graph.add_edge(pydot.Edge(child, i, color="lightblue"))
                    elif self.__nodes[child].label == "=":
                        assert len(self.__nodes[child].children) == 1
                        newChild = self.__nodes[child].children[0]
                        # print(f"bypassing {child} to {newChild}")
                        graph.add_edge(pydot.Edge(newChild, i))
                    else:
                        graph.add_edge(pydot.Edge(child, i))
                if node.label == "cur_state" or node.label == "next_state":
                    subgraphFSM.add_node(
                        pydot.Node(
                            i, label=node.label, style="filled", fillcolor="lightblue"
                        )
                    )
                elif node.label == "=":
                    # bypass assign
                    assert len(node.children) == 1
                    newChild = node.children[0]
                    # print(f"bypassing {i} to {newChild}")
                    continue
                else:
                    subgraphOther.add_node(pydot.Node(i, label=node.label))

            graph.add_subgraph(subgraphFSM)
            graph.add_subgraph(subgraphOther)

            graph.write(dotFile, format="dot")
