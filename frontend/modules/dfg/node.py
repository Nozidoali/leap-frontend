#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 23:59:53
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-24 01:11:59
"""

from typing import Any, List, Dict, Set, Optional
from dataclasses import dataclass, field
from enum import Enum, auto


class OPType(Enum):
    # Automatically generate lowercase value for each enum member
    def _generate_next_value_(name, *_):
        return name.lower()

    # Binary operations
    BINARY_AND = auto()
    BINARY_OR = auto()
    BINARY_BITAND = auto()
    BINARY_XOR = auto()
    BINARY_XNOR = auto()
    BINARY_BITOR = auto()
    BINARY_EQ = auto()
    BINARY_NEQ = auto()
    BINARY_EQ_EXT = auto()
    BINARY_NEQ_EXT = auto()
    BINARY_LT = auto()
    BINARY_GT = auto()
    BINARY_LEQ = auto()
    BINARY_GEQ = auto()
    BINARY_RSHIFT = auto()
    BINARY_RSHIFT_EXT = auto()
    BINARY_LSHIFT = auto()
    BINARY_LSHIFT_EXT = auto()

    # Binary event operations
    BINARY_EVENT_AND = auto()
    BINARY_EVENT_OR = auto()

    # Arithmetic operations
    BINARY_ADD = auto()
    BINARY_SUB = auto()
    BINARY_MUL = auto()
    BINARY_DIV = auto()
    BINARY_MOD = auto()
    BINARY_POW = auto()

    # Unary operations
    UNARY_POS = auto()
    UNARY_NEG = auto()
    UNARY_NOT = auto()
    UNARY_INV = auto()
    UNARY_AND = auto()
    UNARY_OR = auto()
    UNARY_XOR = auto()
    UNARY_NAND = auto()
    UNARY_NOR = auto()
    UNARY_XNOR = auto()
    CONDITIONAL_EXPRESSION = auto()

    # Unary event operations
    UNARY_POSEDGE = auto()
    UNARY_NEGEDGE = auto()

    # Constants
    VARIABLE = auto()
    CONSTANT = auto()
    MACRO = auto()

    # Array operations
    ARRAY_CONCAT = auto()
    ARRAY_REPLICATE = auto()
    ARRAY_SLICE = auto()
    ARRAY_INDEX = auto()

    # Special operations
    FUNCTION_CALL = auto()

    # Event operations
    EVENT_INIT = auto()
    EVENT_COMB = auto()
    EVENT_ALWAYS = auto()

    # Miscellaneous
    UNKNOWN = auto()
    BLACKBOX = auto()

    # Assignments
    ASSIGN = auto()


opPrecedence: Dict[OPType, int] = {
    # Parentheses have the highest precedence
    # Unary reduction operators (highest precedence)
    OPType.UNARY_AND: 1,
    OPType.UNARY_OR: 1,
    OPType.UNARY_XOR: 1,
    OPType.UNARY_NAND: 1,
    OPType.UNARY_NOR: 1,
    OPType.UNARY_XNOR: 1,
    # Unary operators
    OPType.UNARY_POS: 2,
    OPType.UNARY_NEG: 2,
    OPType.UNARY_NOT: 2,
    OPType.UNARY_INV: 2,
    # Power operator
    OPType.BINARY_POW: 3,
    # Arithmetic operators
    OPType.BINARY_MUL: 4,
    OPType.BINARY_DIV: 4,
    OPType.BINARY_MOD: 4,
    # Addition and subtraction
    OPType.BINARY_ADD: 5,
    OPType.BINARY_SUB: 5,
    # Shift operators
    OPType.BINARY_RSHIFT: 6,
    OPType.BINARY_RSHIFT_EXT: 6,
    OPType.BINARY_LSHIFT: 6,
    OPType.BINARY_LSHIFT_EXT: 6,
    # Comparison operators
    OPType.BINARY_LT: 7,
    OPType.BINARY_GT: 7,
    OPType.BINARY_LEQ: 7,
    OPType.BINARY_GEQ: 7,
    # Equivalence operators
    OPType.BINARY_EQ: 8,
    OPType.BINARY_NEQ: 8,
    OPType.BINARY_EQ_EXT: 8,
    OPType.BINARY_NEQ_EXT: 8,
    # Bitwise operators
    OPType.BINARY_BITAND: 9,
    OPType.BINARY_XOR: 9,
    OPType.BINARY_XNOR: 9,
    OPType.BINARY_BITOR: 9,
    # Logical operators
    OPType.BINARY_AND: 9,
    OPType.BINARY_OR: 9,
    # Conditional expression
    OPType.CONDITIONAL_EXPRESSION: 12,
    # Function calls
    OPType.FUNCTION_CALL: 13,
    # Constants, variables, and assignments (lowest precedence)
    OPType.VARIABLE: 0,
    OPType.CONSTANT: 0,
    OPType.MACRO: 0,
    OPType.ASSIGN: 0,
}

opAssociativity: Set = {
    OPType.BINARY_ADD,  # Addition: (a + b) + c == a + (b + c)
    OPType.BINARY_MUL,  # Multiplication: (a * b) * c == a * (b * c)
    OPType.BINARY_BITAND,  # Bitwise AND: (a & b) & c == a & (b & c)
    OPType.BINARY_BITOR,  # Bitwise OR: (a | b) | c == a | (b | c)
    OPType.BINARY_XOR,  # Bitwise XOR: (a ^ b) ^ c == a ^ (b ^ c)
    OPType.BINARY_XNOR,  # Bitwise XNOR: (a ~^ b) ~^ c == a ~^ (b ~^ c)
    OPType.BINARY_AND,  # Logical AND: (a && b) && c == a && (b && c)
    OPType.BINARY_OR,  # Logical OR: (a || b) || c == a || (b || c)
}


def getOpType(op: str) -> OPType:
    for opType in OPType:
        if opType.value == op:
            return opType
    return OPType.UNKNOWN


@dataclass
class Range:
    start: Any
    end: Optional[Any] = None

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Range):
            print(f"Expected Range, got {type(value)}")
            return False
        if self.end is None and value.end is not None:
            print(f"End mismatch: {self.end} != {value.end}")
            return False
        if self.start is None and value.start is not None:
            print(f"Start mismatch: {self.start} != {value.start}")
            return False
        if self.start != value.start or self.end != value.end:
            print(
                f"Range mismatch: {self.start.toString()} != {value.start.toString()}, {self.end.toString()} != {value.end.toString()}"
            )
            return False
        return True

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

    def __repr__(self) -> str:
        return f"Range({self.start}, {self.end})"

    def toWidth(self) -> int:
        if not isinstance(self.start, ConstantNode) or not isinstance(
            self.end, ConstantNode
        ):
            raise Exception(
                f"Expected ConstantNode, got {type(self.start)} and {type(self.end)}"
            )
        startVal = int(self.start.variable_name)
        endVal = int(self.end.variable_name)
        if endVal != 0:
            raise Exception(f"Expected 0, got {endVal}")
        return startVal + 1


class BasicRange(Range):
    def __init__(self, width: int) -> None:
        super().__init__(ConstantNode(width - 1), ConstantNode(0))


def rangeToString(range: Range) -> str:
    if range is None:
        return ""
    assert isinstance(range, Range), f"Expected Range, got {type(range)}"
    return (
        f"[{range.start.toString()}:{range.end.toString()}]"
        if range.end is not None
        else f"[{range.start}]"
    )


@dataclass
class BNode:
    variable_name: str = str(field(default_factory=str))
    range: Optional[Range] = None
    children: List["BNode"] = field(default_factory=list)

    def isVariable(self) -> bool:
        return self.operation == OPType.VARIABLE

    def isConstant(self) -> bool:
        return self.operation == OPType.CONSTANT

    def isOperation(self) -> bool:
        return not self.isVariable() and not self.isConstant()

    def setRange(self, range: Range):
        self.range = range

    def toString(self) -> str:
        return self.variable_name

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, BNode):
            print(f"Expected BNode, got {type(value)}")
            return False
        if self.operation != value.operation:
            print(f"Operation mismatch: {self.operation} != {value.operation}")
            return False
        if str(self.variable_name) != str(value.variable_name):
            print(
                f"Variable name mismatch: {self.variable_name} != {value.variable_name}"
            )
            return False
        if self.range != value.range:
            print(f"Range mismatch: {self.range} != {value.range}")
            return False
        if len(self.children) != len(value.children):
            print(
                f"Number of children mismatch: {len(self.children)} != {len(value.children)}"
            )
            return False
        for i in range(len(self.children)):
            if self.children[i] != value.children[i]:
                print(f"Child {i} mismatch: {self.children[i]} != {value.children[i]}")
                return False
        return True

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

    @property
    def name(self) -> str:
        return self.variable_name

    @name.setter
    def name(self, name: str):
        self.variable_name = name

    @property
    def needsParentheses(self) -> bool:
        return True

    def replaceVariable(self, old: str, new: str):
        if self.variable_name == old:
            self.variable_name = new
        for child in self.children:
            child.replaceVariable(old, new)

    def copy(self) -> "BNode":
        node = BNode(self.variable_name)
        node.operation = self.operation
        node.range = self.range
        node.children = [child.copy() for child in self.children]
        return node


@dataclass
class OPNode(BNode):
    operation: OPType = OPType.UNKNOWN
    children: List[BNode] = field(default_factory=list)

    def __init__(self, op: str, operation: OPType, *items) -> None:
        # Initialize the parent class with the operation name
        super().__init__(str(op))
        assert operation is not None, f"Operation is None, op = {op}"
        self.operation = operation
        self.children = list(items)

    def toString(self) -> str:
        def _childToString(node: OPNode, child: OPNode) -> str:
            if opPrecedence.get(self.operation, 0) > opPrecedence.get(
                child.operation, 0
            ):
                return f"{child.toString()}"
            # if self.operation == child.operation and self.operation in opAssociativity:
            #     return f"{child.toString()}"
            return f"({child.toString()})"

        opName = self.operation.value
        # Case 1: Binary or unary operation
        if opName.startswith("binary_"):
            assert (
                len(self.children) == 2
            ), f"Expected 2 children, got {len(self.children)}, op = {opName}, they are {self.children}"

            # get the child nodes
            child1 = _childToString(self, self.children[0])
            child2 = _childToString(self, self.children[1])
            return f"{child1} {self.variable_name} {child2}"
        if opName.startswith("unary_"):
            assert (
                len(self.children) == 1
            ), f"Expected 1 child, got {len(self.children)}, op = {opName}, they are {self.children}"
            child = _childToString(self, self.children[0])
            return f"{self.variable_name}{child}"
        # Case 2: Array operations
        match self.operation:
            case OPType.ARRAY_CONCAT:
                return (
                    "{" + ", ".join([child.toString() for child in self.children]) + "}"
                )
            case OPType.ARRAY_REPLICATE:
                return (
                    "{"
                    + self.children[0].toString()
                    + "{"
                    + self.children[1].toString()
                    + "}}"
                )
            case OPType.ARRAY_SLICE:
                return f"{self.children[0].toString()}[{self.children[1].toString()}:{self.children[2].toString()}]"
            case OPType.ARRAY_INDEX:
                return f"{self.children[0].toString()}[{self.children[1].toString()}]"
            case OPType.EVENT_ALWAYS:
                return f"always @({self.children[0].toString()})"
            case OPType.EVENT_INIT:
                return "initial"
            case OPType.EVENT_COMB:
                return "*"
            case OPType.CONDITIONAL_EXPRESSION:
                return f"{self.children[0].toString()} ? {self.children[1].toString()} : {self.children[2].toString()}"
            case OPType.FUNCTION_CALL:
                return f"{self.variable_name}({', '.join([child.toString() for child in self.children])})"
            case OPType.MACRO:
                return f"`{self.children[0].toString()}"
            case OPType.UNKNOWN:
                return self.variable_name
            case _:
                return super().toString()


@dataclass
class VarNode(BNode):
    operation: OPType = OPType.VARIABLE

    def toString(self) -> str:
        return (
            self.variable_name
            if self.range is None
            else f"{self.variable_name}{rangeToString(self.range)}"
        )


@dataclass
class ConstantNode(BNode):
    operation: OPType = OPType.CONSTANT

    def __init__(self, value: Any):
        super().__init__(str(value))


@dataclass
class EmptyEvent(BNode):
    operation: OPType = OPType.EVENT_COMB
    variable_name: str = "*"


@dataclass
class InitEvent(BNode):
    operation: OPType = OPType.EVENT_INIT
    variable_name: str = "initial"


@dataclass
class UndefinedNode(BNode):
    operation: OPType = OPType.UNKNOWN
    variable_name: str = "*"

    def toString(self) -> str:
        raise Exception("Undefined node cannot be converted to string")


@dataclass
class BlackBoxNode(BNode):
    operation: OPType = OPType.BLACKBOX
