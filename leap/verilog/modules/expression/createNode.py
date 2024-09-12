#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-02 01:00:01
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-02 01:02:01
"""

from .dfgNode import *
from .binary import *
from .unary import *
from .special import *
from .array import *


def createVariableNode(variable_name: str):
    if isinstance(variable_name, DFGNode):
        assert variable_name.isVariable(), f"variable_name = {variable_name}"
        assert isinstance(
            variable_name.variable_name, str
        ), f"variable_name = {variable_name}"
        return variable_name

    assert isinstance(variable_name, str), f"variable_name = {variable_name}"
    node = DFGNode(variable_name)
    node.operation = SOPType.VARIABLE
    return node


def createConstantNode(value: int):
    node = DFGNode(str(value))
    node.operation = SOPType.CONST
    return node


def createMacroNode(macro_name: str):
    childNode = DFGNode(macro_name)
    childNode.operation = SOPType.CONST

    node = DFGNode("`")
    node.operation = UOPType.MACRO
    node.children = [childNode]
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
    assignFrom: DFGNode, assignTo: DFGNode, condition: DFGNode = None
):
    node = DFGNode("=")
    if condition:
        node.variable_name = "?="
        node.operation = SOPType.CONDITIONAL_ASSIGN
        node.children = [condition, assignFrom]
    elif condition is None:
        node.operation = SOPType.ASSIGN
        node.children = [assignFrom]

    assert isinstance(assignTo, DFGNode), f"assignTo = {assignTo}"
    assert assignTo.isVariable(), f"assignTo = {assignTo}"
    outputNode = createVariableNode(assignTo)
    outputNode.children = [node]
    return outputNode


def createAssignNodes(
    assignFrom: DFGNode, assignTo: DFGNode, condition: DFGNode = None
):
    newNodes = []
    node = _createInputAssignNode(assignFrom)
    newNodes.append(node)

    assert isinstance(assignTo, DFGNode)

    if assignTo.isVariable():
        newNodes.append(_createOutputAssignNode(node, assignTo, condition))
    elif assignTo.isConstant():
        raise ValueError(f"assignTo = {assignTo}")
    else:
        raise ValueError(f"assignTo = {assignTo}")

    return newNodes


def createArraySlicingNode(arrayName: str, indexFrom: DFGNode, indexTo: DFGNode):
    # node = DFGNode(AOPType.SLICE.value)
    # node.operation = AOPType.SLICE
    # node.children = [arrayName, indexFrom, indexTo]
    # return node
    assert isinstance(arrayName, str)
    node = createVariableNode(arrayName)
    node.setRange(Range(indexFrom, indexTo))
    return node


def createArrayIndexingNode(arrayName: str, index: DFGNode):
    # node = DFGNode(AOPType.INDEX.value)
    # node.operation = AOPType.INDEX
    # node.children = [arrayName, index]
    # return node
    assert isinstance(arrayName, str)
    node = createVariableNode(arrayName)
    node.setRange(Range(index))
    return node


def createMuxNode(variableName, cond: DFGNode, branches: list):
    node = DFGNode(variableName)
    node.operation = SOPType.CONDITIONAL_ASSIGN
    node.children = [cond] + branches
    return node


def createConditionalExpression(
    cond: DFGNode, trueBranch: DFGNode, falseBranch: DFGNode
):
    node = DFGNode("?")
    node.operation = SOPType.CONDITIONAL
    node.children = [cond, trueBranch, falseBranch]
    return node
