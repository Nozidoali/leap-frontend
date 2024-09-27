#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 23:50:49
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:58:28
"""

from lark import Transformer, v_args, Tree
from ...modules import *
from .larkUtils import *


class PortTransformer(Transformer):

    # port_range : "[" expression ":" expression "]"
    @v_args(inline=True)
    def port_range(self, start, end):
        assert isinstance(start, DFGNode), f"start = {start}, type = {type(start)}"
        assert isinstance(end, DFGNode), f"end = {end}, type = {type(end)}"
        return Range(start, end)

    def variable_list(self, items):
        return items

    # declaration: [port_direction] [port_type] [port_range] variable_list ["=" expression] ";"
    def declaration(self, items):
        statements = []
        dir, t, range, variables, expression = items
        dir = PortDirection.fromString(dir.data) if dir is not None else None
        t = PortType.fromString(t.data) if t is not None else PortType.WIRE
        ports = []
        for variable in variables:
            port = Port(variable)
            port.setAll(dir, t, range)
            if expression:
                assert len(variables) == 1
                statements.append(BlockingAssignment(variable, expression))
            ports.append(port)
        statements.append(PortDeclaration(ports))
        return statements
