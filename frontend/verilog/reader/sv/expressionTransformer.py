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

    # constant nodes
    def extended_based_number(self, items):
        return ConstantNode(items[0])

    def regular_number(self, items):
        return ConstantNode(items[0])

    def string(self, items):
        return ConstantNode(items[0])

    def based_number(self, items):
        return ConstantNode(items[0])

    def macro_usage(self, items):
        return OPNode("`", NodeType.MACRO, ConstantNode(items[0]))

    def variable_expression(self, items):
        return VarNode(items[0])

    # array nodes
    def concatenation(self, items):
        return OPNode("{{{}}}", NodeType.ARRAY_CONCAT, items)

    def repeated_concatenation(self, items):
        # TODO: i think this is wrong
        return OPNode("{n{}}", NodeType.ARRAY_REPLICATE, items[0], items[1])

    def array_slicing(self, items):
        return OPNode("[]", NodeType.ARRAY_SLICE, items[0], items[1])

    def array_indexing(self, items):
        return OPNode("[]", NodeType.ARRAY_INDEX, items[0], items[1])

    def array_concat(self, items):
        return OPNode("{,}", NodeType.ARRAY_CONCAT, *items)

    def array_replicate(self, items):
        return OPNode("{n{}}", NodeType.ARRAY_REPLICATE, items[0], items[1])

    def array_slice(self, items):
        return OPNode("[]", NodeType.ARRAY_SLICE, items[0], items[1])

    def array_index(self, items):
        return OPNode("[]", NodeType.ARRAY_INDEX, items[0], items[1])

    def function_call(self, items):
        return OPNode("()", NodeType.FUNCTION_CALL, VarNode(items[0]), *items[1])

    def function_parameters(self, items):
        return items

    def dollar_indentifier(self, items):
        return str(items[0])

    # expression nodes
    def expression(self, items):
        return items[0]
    
    def lhs_expression(self, items):
        return items[0]

    def binary_and(self, items):
        return OPNode("&&", NodeType.BINARY_AND, *items)

    def binary_or(self, items):
        return OPNode("||", NodeType.BINARY_OR, *items)

    def binary_bitand(self, items):
        return OPNode("&", NodeType.BINARY_BITAND, *items)

    def binary_xor(self, items):
        return OPNode("^", NodeType.BINARY_XOR, *items)

    def binary_xnor(self, items):
        return OPNode("^~", NodeType.BINARY_XNOR, *items)

    def binary_bitor(self, items):
        return OPNode("|", NodeType.BINARY_BITOR, *items)

    def binary_eq(self, items):
        return OPNode("==", NodeType.BINARY_EQ, *items)

    def binary_neq(self, items):
        return OPNode("!=", NodeType.BINARY_NEQ, *items)

    def binary_eq_ext(self, items):
        return OPNode("===", NodeType.BINARY_EQ_EXT, *items)

    def binary_neq_ext(self, items):
        return OPNode("!==", NodeType.BINARY_NEQ_EXT, *items)

    def binary_lt(self, items):
        return OPNode("<", NodeType.BINARY_LT, *items)

    def binary_gt(self, items):
        return OPNode(">", NodeType.BINARY_GT, *items)

    def binary_leq(self, items):
        return OPNode("<=", NodeType.BINARY_LEQ, *items)

    def binary_geq(self, items):
        return OPNode(">=", NodeType.BINARY_GEQ, *items)

    def binary_rshift(self, items):
        return OPNode(">>", NodeType.BINARY_RSHIFT, *items)

    def binary_rshift_ext(self, items):
        return OPNode(">>>", NodeType.BINARY_RSHIFT_EXT, *items)

    def binary_lshift(self, items):
        return OPNode("<<", NodeType.BINARY_LSHIFT, *items)

    def binary_lshift_ext(self, items):
        return OPNode("<<<", NodeType.BINARY_LSHIFT_EXT, *items)

    def binary_add(self, items):
        return OPNode("+", NodeType.BINARY_ADD, *items)

    def binary_sub(self, items):
        return OPNode("-", NodeType.BINARY_SUB, *items)
    
    def binary_mul(self, items):
        return OPNode("*", NodeType.BINARY_MUL, *items)

    def binary_div(self, items):
        return OPNode("/", NodeType.BINARY_DIV, *items)
    
    def binary_mod(self, items):
        return OPNode("%", NodeType.BINARY_MOD, *items)

    def unary_pos(self, items):
        return OPNode("+", NodeType.UNARY_POS, *items)

    def unary_neg(self, items):
        return OPNode("-", NodeType.UNARY_NEG, *items)

    def unary_not(self, items):
        return OPNode("!", NodeType.UNARY_NOT, *items)

    def unary_inv(self, items):
        return OPNode("~", NodeType.UNARY_INV, *items)

    def unary_and(self, items):
        return OPNode("&", NodeType.UNARY_AND, *items)

    def unary_or(self, items):
        return OPNode("|", NodeType.UNARY_OR, *items)

    def unary_xor(self, items):
        return OPNode("^", NodeType.UNARY_XOR, *items)

    def unary_nand(self, items):
        return OPNode("~&", NodeType.UNARY_NAND, *items)

    def unary_nor(self, items):
        return OPNode("~|", NodeType.UNARY_NOR, *items)

    def unary_xnor(self, items):
        return OPNode("~^", NodeType.UNARY_XNOR, *items)

    def conditional_expression(self, items):
        return OPNode("?:", NodeType.CONDITIONAL_EXPRESSION, *items)
