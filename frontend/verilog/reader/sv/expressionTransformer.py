#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 11:36:22
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 12:45:25
"""

from lark import Transformer, v_args
from ...modules import *


class ExpressionTransformer(Transformer):

    def lhs_expression(self, items):
        return items[0]

    def expression(self, items):
        return items[0]

    def constant_node(self, items):
        return ConstantNode(items[0])

    # constant nodes
    extended_based_number = regular_number = string = based_number = constant_node

    def macro_usage(self, items):
        return OPNode("`", OPType.MACRO, ConstantNode(items[0]))

    def variable(self, items):
        return VarNode(items[0])

    # Generalized operation helper (for all types of operations)
    def op_node(self, symbol, op_type, items):
        return OPNode(symbol, op_type, *items)

    # Unified operations dictionary (binary, unary, array, and conditional)
    operations = {
        # Binary operations
        OPType.BINARY_AND: "&&",
        OPType.BINARY_OR: "||",
        OPType.BINARY_BITAND: "&",
        OPType.BINARY_XOR: "^",
        OPType.BINARY_XNOR: "^~",
        OPType.BINARY_BITOR: "|",
        OPType.BINARY_EQ: "==",
        OPType.BINARY_NEQ: "!=",
        OPType.BINARY_EQ_EXT: "===",
        OPType.BINARY_NEQ_EXT: "!==",
        OPType.BINARY_LT: "<",
        OPType.BINARY_GT: ">",
        OPType.BINARY_LEQ: "<=",
        OPType.BINARY_GEQ: ">=",
        OPType.BINARY_RSHIFT: ">>",
        OPType.BINARY_RSHIFT_EXT: ">>>",
        OPType.BINARY_LSHIFT: "<<",
        OPType.BINARY_LSHIFT_EXT: "<<<",
        OPType.BINARY_ADD: "+",
        OPType.BINARY_SUB: "-",
        OPType.BINARY_MUL: "*",
        OPType.BINARY_DIV: "/",
        OPType.BINARY_MOD: "%",
        OPType.BINARY_POW: "**",
        # Unary operations
        OPType.UNARY_POS: "+",
        OPType.UNARY_NEG: "-",
        OPType.UNARY_NOT: "!",
        OPType.UNARY_INV: "~",
        OPType.UNARY_AND: "&",
        OPType.UNARY_OR: "|",
        OPType.UNARY_XOR: "^",
        OPType.UNARY_NAND: "~&",
        OPType.UNARY_NOR: "~|",
        OPType.UNARY_XNOR: "~^",
        # Array operations
        OPType.ARRAY_CONCAT: "{{{}}}",
        OPType.ARRAY_REPLICATE: "{n{}}",
        OPType.ARRAY_SLICE: "[]",
        OPType.ARRAY_INDEX: "[]",
        # Conditional expression
        OPType.CONDITIONAL_EXPRESSION: "?:",
    }

    # Dynamically generate methods for all operations
    for op_type, symbol in operations.items():
        locals()[f"{op_type.name.lower()}"] = (
            lambda self, items, s=symbol, t=op_type: self.op_node(s, t, items)
        )

    def function_call(self, items):
        return OPNode("()", OPType.FUNCTION_CALL, VarNode(items[0]), *items[1])

    def function_parameters(self, items):
        return items

    def dollar_identifier(self, items):
        return str(items[0])
