#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 23:59:53
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-24 01:11:59
"""

from typing import Any


class Range:
    def __init__(self, start: int, end: int = None):
        self.start = start
        self.end = end


def rangeToString(range: Range) -> str:
    if range is None:
        return ""
    assert isinstance(range, Range), f"Expected Range, got {type(range)}"
    return (
        f"[{range.start}:{range.end}]" if range.end is not None else f"[{range.start}]"
    )


class DFGNode:
    # Expressions are hard to handle because of the recursive nature

    def __init__(self, name: str = None) -> None:
        self.variable_name = name
        self.operation = None
        self.range = None
        self.children = []

    def __repr__(self) -> str:
        return f"Node({self.variable_name})"

    def isVariable(self):
        return self.operation == NodeType.VARIABLE

    def isConstant(self):
        return self.operation == NodeType.CONSTANT

    def setRange(self, range: Range):
        self.range = range

    def toString(self) -> str:
        return (
            self.variable_name
            if self.range is None
            else f"{self.variable_name}{rangeToString(self.range)}"
        )

    @property
    def name(self):
        return self.variable_name

    @property
    def needsParentheses(self):
        return True

    def replaceVariable(self, old: str, new: str):
        if self.variable_name == old:
            self.variable_name = new
        child: DFGNode
        for child in self.children:
            child.replaceVariable(old, new)

    def copy(self):
        node = DFGNode(self.variable_name)
        node.operation = self.operation
        node.range = self.range
        for child in self.children:
            node.children.append(child.copy())
        return node


from enum import Enum


class NodeType(Enum):
    BINARY_AND = "binary_and"
    BINARY_OR = "binary_or"
    BINARY_BITAND = "binary_bitand"
    BINARY_XOR = "binary_xor"
    BINARY_XNOR = "binary_xnor"
    BINARY_BITOR = "binary_bitor"
    BINARY_EQ = "binary_eq"
    BINARY_NEQ = "binary_neq"
    BINARY_EQ_EXT = "binary_eq_ext"
    BINARY_NEQ_EXT = "binary_neq_ext"
    BINARY_LT = "binary_lt"
    BINARY_GT = "binary_gt"
    BINARY_LEQ = "binary_leq"
    BINARY_GEQ = "binary_geq"
    BINARY_RSHIFT = "binary_rshift"
    BINARY_RSHIFT_EXT = "binary_rshift_ext"
    BINARY_LSHIFT = "binary_lshift"
    BINARY_LSHIFT_EXT = "binary_lshift_ext"
    
    # Arithmetic operations
    BINARY_ADD = "binary_add"
    BINARY_SUB = "binary_sub"
    BINARY_MUL = "binary_mul"
    BINARY_DIV = "binary_div"
    BINARY_MOD = "binary_mod"
    
    # Unary operations
    UNARY_POS = "unary_pos"
    UNARY_NEG = "unary_neg"
    UNARY_NOT = "unary_not"
    UNARY_INV = "unary_inv"
    UNARY_AND = "unary_and"
    UNARY_OR = "unary_or"
    UNARY_XOR = "unary_xor"
    UNARY_NAND = "unary_nand"
    UNARY_NOR = "unary_nor"
    UNARY_XNOR = "unary_xnor"
    CONDITIONAL_EXPRESSION = "conditional_expression"

    VARIABLE = "variable"
    CONSTANT = "constant"
    MACRO = "macro"

    ARRAY_CONCAT = "array_concat"
    ARRAY_REPLICATE = "array_replicate"
    ARRAY_SLICE = "array_slice"
    ARRAY_INDEX = "array_index"

    FUNCTION_CALL = "function_call"


class OPNode(DFGNode):
    def __init__(self, op: str, operation: NodeType, *children) -> None:
        super().__init__(op)
        self.operation = operation
        self.children = children


class VarNode(DFGNode):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.operation = NodeType.VARIABLE


class ConstantNode(DFGNode):
    def __init__(self, value: Any) -> None:
        super().__init__(str(value))
        self.operation = NodeType.CONSTANT
