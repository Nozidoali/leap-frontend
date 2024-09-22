#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 11:36:22
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 12:45:25
"""

from lark import Transformer
from ...modules import *


class ExpressionTransformer(Transformer):
    
    def unary_expression(self, items):
        return items
    
    def binary_expression(self, items):
        return items
    
    def extended_based_number(self, items):
        return ConstantNode(items[0])

    def regular_number(self, items):
        return ConstantNode(items[0])

    def macro_usage(self, items):
        return MacroNode(ConstantNode(items[0]))

    def concatenation(self, items):
        return ConcatOpNode(items)

    def repeated_concatenation(self, items):
        # TODO: i think this is wrong
        return ConcatOpNode([items[1]])

    def string(self, items):
        return ConstantNode(items[0])

    def function_call(self, items):
        return FuncNode(items[0], items[1:])

    def function_parameters(self, items):
        return items

    def dollar_indentifier(self, items):
        return str(items[0])

    def array_slicing(self, items):
        return ArrayOpNode(items[0], items[1], items[2])

    def array_indexing(self, items):
        return ArrayOpNode(items[0], items[1])

    def expression(self, items):
        # we transform the expression to a pygraphviz graph
        if len(items) == 3:
            # binary operation
            opName = items[1].data
            if isinstance(items[0], DFGNode):
                return BinaryOpNode(opName, items[0], items[2])
            return items[1]
        if len(items) == 2:
            # unary operation
            opName = items[0].data
            return UnaryOpNode(opName, items[1])
        if isinstance(items[0], str):
            # this is a variable
            return VariableNode(items[0])
        if isinstance(items[0], DFGNode):
            return items[0]
        return items[0]

    # conditional_expression: expression "?" expression ":" expression
    def conditional_expression(self, items):
        return MuxNode(items[0], items[1], items[2])
