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
    def __init__(self, start: Any, end: Any = None):
        self.start = start
        self.end = end

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Range):
            return False
        if self.end is None and value.end is not None:
            return
        if self.start is None and value.start is not None:
            return False
        return self.start == value.start and self.end == value.end

    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"


def rangeToString(range: Range) -> str:
    if range is None:
        return ""
    assert isinstance(range, Range), f"Expected Range, got {type(range)}"
    return (
        f"[{range.start.toString()}:{range.end.toString()}]"
        if range.end is not None
        else f"[{range.start}]"
    )


class DFGNode:
    # Expressions are hard to handle because of the recursive nature

    def __init__(self, name: str = None) -> None:
        self.variable_name: str = str(name)  # could be a Tree object
        self.operation: OPType = None
        self.range: Range = None
        self.children: list = []

    def __repr__(self) -> str:
        return f"Node({self.variable_name})"

    def isVariable(self) -> bool:
        return self.operation == OPType.VARIABLE

    def isConstant(self) -> bool:
        return self.operation == OPType.CONSTANT

    def setRange(self, range: Range):
        self.range = range

    def toString(self) -> str:
        print(f"toString not implemented for {self}, op = {self.operation}")
        raise NotImplementedError

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, DFGNode):
            return False
        if self.operation != value.operation:
            return False
        if self.variable_name != value.variable_name:
            return False
        if self.range != value.range:
            return False
        if len(self.children) != len(value.children):
            return False
        for i in range(len(self.children)):
            if self.children[i] != value.children[i]:
                return False
        return True

    @property
    def name(self) -> str:
        return self.variable_name

    @property
    def needsParentheses(self) -> bool:
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


class OPType(Enum):
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
    BINARY_POW = "binary_pow"

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

    EVENT_INIT = "event_init"
    EVENT_COMB = "event_comb"

    UNARY_POSEDGE = "unary_posedge"
    UNARY_NEGEDGE = "unary_negedge"

    BINARY_EVENT_AND = "binary_event_and"
    BINARY_EVENT_OR = "binary_event_or"

    EVENT_ALWAYS = "event_always"

    UNKNOWN = "unknown"


class OPNode(DFGNode):
    def __init__(self, op: str, operation: OPType, *children) -> None:
        super().__init__(op)
        self.operation = operation
        self.children = children

    def toString(self) -> str:
        opName = self.operation.value
        if opName.startswith("binary_"):
            return f"({self.children[0].toString()} {self.variable_name} {self.children[1].toString()})"
        if opName.startswith("unary_"):
            return f"({self.variable_name} {self.children[0].toString()})"
        match self.operation:
            # Case 1
            # Array operations
            case OPType.ARRAY_CONCAT:
                return f"{{{', '.join([child.toString() for child in self.children])}}}"
            case OPType.ARRAY_REPLICATE:
                return (
                    f"{{{self.children[0].toString()}{{self.children[1].toString()}}}}"
                )
            case OPType.ARRAY_SLICE:
                return f"{self.children[0].toString()}[{self.children[1].toString()}:{self.children[2].toString()}]"
            case OPType.ARRAY_INDEX:
                return f"{self.children[0].toString()}[{self.children[1].toString()}]"
            # Case 2
            # Event operations
            case OPType.EVENT_ALWAYS:
                return f"always @({self.children[0].toString()})"
            case OPType.EVENT_INIT:
                return "initial"
            case OPType.EVENT_COMB:
                return "*"
            # Case 3
            # Special operations
            case OPType.CONDITIONAL_EXPRESSION:
                return f"({self.children[0].toString()} ? {self.children[1].toString()} : {self.children[2].toString()})"
            case OPType.FUNCTION_CALL:
                return f"{self.variable_name}({', '.join([child.toString() for child in self.children])})"
            case OPType.MACRO:
                return f"`{self.children[0].toString()}"
            case OPType.UNKNOWN:
                return self.variable_name
            case _:
                print(f"Unsupported operation {self.operation}")
                raise Exception(f"Unsupported operation {self.operation}")


class VarNode(DFGNode):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.operation = OPType.VARIABLE

    def toString(self) -> str:
        return (
            self.variable_name
            if self.range is None
            else f"{self.variable_name}{rangeToString(self.range)}"
        )


class ConstantNode(DFGNode):
    def __init__(self, value: Any) -> None:
        super().__init__(str(value))
        self.operation = OPType.CONSTANT

    def toString(self) -> str:
        return self.variable_name


class EmptyEvent(DFGNode):
    def __init__(self) -> None:
        super().__init__("*")
        self.operation = OPType.EVENT_COMB

    def toString(self) -> str:
        return "*"


class InitEvent(DFGNode):
    def __init__(self) -> None:
        super().__init__("initial")
        self.operation = OPType.EVENT_INIT

    def toString(self) -> str:
        return "initial"


class UndefinedNode(DFGNode):
    def __init__(self) -> None:
        super().__init__("*")
        self.operation = OPType.UNKNOWN

    def toString(self) -> str:
        raise Exception("Undefined node cannot be converted to string")
