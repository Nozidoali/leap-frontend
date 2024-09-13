#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 11:36:22
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 12:45:25
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args, Tree
from ...modules import *


class ExpressionTransformer(Transformer):
    def extended_based_number(self, items):
        return createConstantNode(items[0])

    def regular_number(self, items):
        return createConstantNode(items[0])

    def macro_usage(self, items):
        return createMacroNode(items[0])

    def concatenation(self, items):
        return createConcatOpNode(items)

    def repeated_concatenation(self, items):
        return createConcatOpNode([items[1]])

    def string(self, items):
        return DFGNode(items[0])

    def function_call(self, items):
        function_name = items[0]
        return createFuncCallNode(function_name, items[1:])

    def function_parameters(self, items):
        return items

    def dollar_indentifier(self, items):
        return str(items[0])

    def array_slicing(self, items):
        return createArraySlicingNode(items[0], items[1], items[2])

    def array_indexing(self, items):
        return createArrayIndexingNode(items[0], items[1])

    def expression(self, items):
        # we transform the expression to a pygraphviz graph
        if len(items) == 3:
            # binary operation
            opName = items[1].data
            if isinstance(items[0], DFGNode):
                return createBinaryOpNode(opName, items[0], items[2])
            logger.error(f"items = {items}")
            return items[1]

        if len(items) == 2:
            # unary operation
            opName = items[0].data
            return createUnaryOpNode(opName, items[1])

        if isinstance(items[0], str):
            # this is a variable
            return createVariableNode(items[0])

        if isinstance(items[0], DFGNode):
            return items[0]

        logger.error(f"items = {items}")

        return items[0]

    # conditional_expression: expression "?" expression ":" expression
    def conditional_expression(self, items):
        return createConditionalExpression(items[0], items[1], items[2])
