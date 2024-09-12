#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 23:59:53
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-24 01:11:59
"""

from .binary import *
from .unary import *
from .special import *
from .array import *


class Range:
    def __init__(self, start: int, end: int = None):
        self.start = start
        self.end = end

    def __repr__(self) -> str:
        startStr = None
        if isinstance(self.start, DFGNode):
            startStr = dfgNodeToString(self.start)
        else:
            assert isinstance(self.start, int), "start should be an integer"
            startStr = str(self.start)

        if self.end is None:
            return f"[{startStr}]"

        endStr = None
        if isinstance(self.end, DFGNode):
            endStr = dfgNodeToString(self.end)
        else:
            assert isinstance(self.end, int), "end should be an integer"
            endStr = str(self.end)

        return f"[{startStr}:{endStr}]"


class DFGNode:
    # Expressions are hard to handle because of the recursive nature

    def __init__(self, variable_name: str = None) -> None:
        self.variable_name = variable_name
        self.range = None
        self.operation = None
        self.children = []

    def __repr__(self) -> str:
        return self.variable_name

    def __str__(self) -> str:
        return dfgNodeToString(self)

    def isVariable(self):
        return self.operation == SOPType.VARIABLE

    def isConstant(self):
        return self.operation == SOPType.CONST

    def setRange(self, range: Range):
        self.range = range


def dfgNodeToString(node: DFGNode) -> str:
    # this is a recursive function
    if node.isConstant():
        return node.variable_name

    if node.isVariable():
        if node.range is not None:
            return f"{node.variable_name}{node.range}"
        return node.variable_name

    if isinstance(node.operation, BOPType):
        leftOp = dfgNodeToString(node.children[0])
        if not node.children[0].isVariable() and not node.children[0].isConstant():
            # we need to wrap the expression in parentheses
            if node.children[0].operation != UOPType.MACRO:
                leftOp = f"({leftOp})"
        rightOp = dfgNodeToString(node.children[1])
        if not node.children[1].isVariable() and not node.children[1].isConstant():
            # we need to wrap the expression in parentheses
            if node.children[1].operation != UOPType.MACRO:
                rightOp = f"({rightOp})"

        # check the operation
        if node.children[1].isConstant() and node.operation not in [
            BOPType.EQUAL,
            BOPType.NEQ,
            BOPType.LT,
            BOPType.LEQ,
            BOPType.GT,
            BOPType.GEQ,
        ]:
            # we skip the spaces
            return f"{leftOp}{node.variable_name}{rightOp}"

        return f"{leftOp} {node.variable_name} {rightOp}"

    if isinstance(node.operation, UOPType):
        if node.variable_name == "`":
            return f"`{dfgNodeToString(node.children[0])}"
        if node.children[0].isVariable():
            return f"{node.variable_name}{dfgNodeToString(node.children[0])}"
        if node.children[0].isConstant():
            return f"{node.variable_name}{dfgNodeToString(node.children[0])}"
        return f"{node.variable_name}({dfgNodeToString(node.children[0])})"

    if isinstance(node.operation, AOPType):
        if node.operation == AOPType.INDEX:
            return f"{dfgNodeToString(node.children[0])}[{dfgNodeToString(node.children[1])}]"
        if node.operation == AOPType.SLICE:
            return f"{dfgNodeToString(node.children[0])}[{dfgNodeToString(node.children[1])}:{dfgNodeToString(node.children[2])}]"

    if isinstance(node.operation, SOPType):
        if node.operation == SOPType.CONCAT:
            return (
                "{"
                + ", ".join([dfgNodeToString(child) for child in node.children])
                + "}"
            )
        if node.operation == SOPType.FUNCTION:
            return (
                f"${node.variable_name}("
                + ", ".join([dfgNodeToString(child) for child in node.children])
                + ")"
            )
        if node.operation == SOPType.CONDITIONAL:
            return f"{dfgNodeToString(node.children[0])} ? {dfgNodeToString(node.children[1])} : {dfgNodeToString(node.children[2])}"

    print(f"node {node.variable_name} has unknown operation {node.operation}")
    raise NotImplementedError
