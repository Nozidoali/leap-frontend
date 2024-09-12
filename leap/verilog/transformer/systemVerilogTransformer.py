#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 19:20:27
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:51:31
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args, Tree
from ..modules import *
from .sv import *


class SystemVerilogTransformer(
    ModuleTransformer,
    DeclarationTransformer,
    StatementTransformer,
    PortTransformer,
    ExpressionTransformer,
    FSMTransformer,
    EventTransformer,
    NetlistTransformer,
):
    def start(self, items):
        return items[0]

    # ?description: (macro_definition | timescale_directive | module)+
    def description(self, items):
        modules = []
        definitions = {}
        for item in items:
            if isinstance(item, Module):
                modules.append(item)
            elif isinstance(item, dict):
                for key, value in item.items():
                    key = str(key)
                    value = str(value)
                    definitions[key] = value
        return Netlist(modules, definitions)

    # timescale_directive: "`timescale" time_unit "/" time_precision
    # time_precision: NUMBER time_identifier
    # time_identifier: "s" | "ms" | "us" | "ns" | "ps"
    def timescale_directive(self, items):
        time_unit = items[0]
        time_precision = items[1]
        return {"time_unit": time_unit, "time_precision": time_precision}

    # time_unit: NUMBER time_identifier
    def time_unit(self, items):
        return TimeValue(float(items[0]), items[1].data)

    def time_precision(self, items):
        return TimeValue(float(items[0]), items[1].data)

    # macro_definition: "`define" identifier macro_body
    # macro_body: /.+/
    def macro_definition(self, items):
        identifier = str(items[0])
        macro_body = str(items[1])
        return {identifier: macro_body}

    def identifier(self, items):
        return items[0]

    def macro_body(self, items):
        return items[0]

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
