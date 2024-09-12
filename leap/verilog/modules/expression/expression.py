#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-02 01:00:01
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-02 01:02:01
"""

from .dfg import DFGraph, DFGNode
from .binary import *
from .unary import *
from .special import *
from .array import *


def createVariableNode(variable_name: str):
    node = DFGNode(variable_name)
    node.operation = SOPType.VARIABLE
    return node


def createConstantNode(value: int):
    node = DFGNode(str(value))
    node.operation = SOPType.CONST
    return node


def createBinaryOpNode(op: BOPType | str, left: DFGNode, right: DFGNode):
    if isinstance(op, str):
        op = BOPType.fromString(op)
    node = DFGNode(str(op.value))
    node.operation = op
    node.children = [left, right]
    return node


def createUnaryOpNode(op: UOPType | str, child: DFGNode):
    if isinstance(op, str):
        op = UOPType.fromString(op)
    node = DFGNode(str(op.value))
    node.operation = op
    node.children = [child]
    return node


def createConcatOpNode(children: list):
    node = DFGNode("\{\}")
    node.operation = SOPType.CONCAT
    assert isinstance(children, list)
    node.children = children
    return node


def createFuncCallNode(func_name: str, children: list):
    node = DFGNode(func_name)
    node.operation = SOPType.FUNCTION
    assert isinstance(children, list)
    node.children = children
    return node


def _createInputAssignNode(assignFrom: DFGNode):
    node = DFGNode("=")
    node.operation = SOPType.WIRE
    node.children = [assignFrom]
    return node


def _createOutputAssignNode(
    assignFrom: DFGNode, assignTo: str, condition: DFGNode = None
):
    node = DFGNode(assignTo)
    if condition is not None:
        node.operation = SOPType.CONDITIONAL_ASSIGN
        node.children = [condition, assignFrom]
    else:
        node.operation = SOPType.ASSIGN
        node.children = [assignFrom]
    return node


def createAssignNodes(
    assignFrom: DFGNode, assignTo: str | DFGNode, condition: DFGNode = None
):
    newNodes = []
    node = _createInputAssignNode(assignFrom)
    newNodes.append(node)

    if isinstance(assignTo, str):
        newNodes.append(_createOutputAssignNode(node, assignTo, condition))
    else:
        child: DFGNode
        for child in assignTo.children:
            assert child.isVariable() or child.isConstant(), f"child = {child}"
            assert child.children == [], f"child = {child}"

            newNodes.append(
                _createOutputAssignNode(node, child.variable_name, condition)
            )

    return newNodes


def createArraySlicingNode(arrayName: DFGNode, indexFrom: DFGNode, indexTo: DFGNode):
    node = DFGNode(AOPType.SLICE.value)
    node.operation = AOPType.SLICE
    node.children = [arrayName, indexFrom, indexTo]
    return node


def createArrayIndexingNode(arrayName: DFGNode, index: DFGNode):
    node = DFGNode(AOPType.INDEX.value)
    node.operation = AOPType.INDEX
    node.children = [arrayName, index]
    return node


def createMuxNode(variableName, cond: DFGNode, branches: list):
    node = DFGNode(variableName)
    node.operation = SOPType.CONDITIONAL_ASSIGN
    node.children = [cond] + branches
    return node
