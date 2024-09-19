#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 14:12:23
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 19:10:29
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args, Tree
from ..modules import *


class VerilogTransformer(Transformer):
    def start(self, items):
        logger.debug("start: %s\n", items)
        if isinstance(items, list):
            return Netlist(items)
        else:
            return Netlist([items])

    def description(self, items):
        # transpass the items
        return items

    # this is a list of lots of items, so we set inline=False
    @v_args(inline=False)
    def module_declaration(self, items):
        """
        module_declaration: [attribute_instances] ("module"|"macromodule") identifier [param_list] [port_list] ";" module_items* "endmodule"
        """
        attribute_instances = items[0]
        module_name = items[1]
        param_list = items[2]
        port_list = items[3]
        module_items = items[4:]
        # transpass the items
        return Module(
            attribute_instances=attribute_instances,
            module_name=module_name,
            param_list=param_list,
            port_list=port_list,
            module_items=module_items,
        )

    @v_args(inline=True)
    def param_assignment(self, range, lvalue, expression):
        """
        param_assignment: ["signed"] [range] lvalue "=" expression
        """
        return Parameter(range=range, name=lvalue, value=expression)

    # we override the default method to return the data directly
    # this requires us to override all the methods without children
    def __default__(self, data, children, meta):
        assert isinstance(data, str)
        # use switch case to handle the data
        match data:
            # These are the AST nodes partially handled
            case "params":
                logger.info(
                    f"children[1:]: \n data = {data}, children = {children}, meta = {meta}"
                )
                return children[:]
            # These are the transparent AST nodes
            case "param_list" | "param_declaration" | "attribute_instances":
                logger.info(
                    f"children[0]: \n data = {data}, children = {children}, meta = {meta}"
                )
                return children[0]
            case _:
                return Tree(data, children, meta)
