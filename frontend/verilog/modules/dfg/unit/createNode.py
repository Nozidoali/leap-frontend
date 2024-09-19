#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-02 01:00:01
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-02 01:02:01
"""

from .node import *
from .op import *
from .range import *
from .constantNode import *
from .variableNode import *

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
    outputNode = VariableNode(assignTo)
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
