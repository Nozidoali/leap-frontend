#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 19:20:27
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:51:31
"""

from ...modules import *
from .expressionTransformer import *
from .conditionTransformer import *
from .portTransformer import *
from .moduleTransformer import *


class VerilogTransformer(
    ModuleTransformer,
    ConditionTransformer,
    PortTransformer,
    ExpressionTransformer,
):
    # description: (macro_definition | timescale_definition | module)+
    def start(self, items):
        netlist = Netlist()
        for item in items:
            if isinstance(item, Module):
                netlist.addModule(item)
            elif isinstance(item, Statement):
                item(netlist)
            else:
                raise ValueError(f"Unknown item {item}")
        return netlist

    # timescale_definition: "`timescale" time_unit "/" time_precision
    # time_precision: NUMBER time_identifier
    # time_identifier: "s" | "ms" | "us" | "ns" | "ps"
    def timescale_definition(self, items):
        val1, pre1, val2, pre2 = items
        return TimeScaleDefinition(
            TimeValue(int(val1), str(pre1.data)), TimeValue(int(val2), str(pre2.data))
        )

    # macro_definition: "`define" identifier macro_body
    # macro_body: /.+/
    def macro_definition(self, items):
        name: str = str(items[0])
        value: DFGNode = items[1]
        return MacroDefinition(name, value)
