#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 23:50:49
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:58:28
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args, Tree
from ...modules import *


class PortTransformer(Transformer):
    # port_declaration: port_header? (extended_port | simple_port)
    # This is a workaround to avoid the ambiguity of the variable numbers of arguments
    @v_args(inline=False)
    def port_declaration(self, items):
        new_ports = []
        if len(items) == 1:
            ports = items[0]
            new_ports.extend(ports)
        elif len(items) == 2:
            port_header: Tree = items[0]
            ports = items[1]
            headerType = port_header.data

            port: Port
            for port in ports:
                new_port = port
                if headerType == "header0":
                    val0 = port_header.children[0].data
                    new_port.setType(val0)
                elif headerType == "header1":
                    val0 = PortDirection.fromString(port_header.children[0].data)
                    new_port.setDirection(val0)
                else:
                    val0 = PortDirection.fromString(port_header.children[0].data)
                    val1 = port_header.children[1].data
                    new_port.setDirection(val0)
                    new_port.setType(val1)
                new_ports.append(new_port)
        else:
            assert False
        return "port_declaration", new_ports

    @v_args(inline=False)
    def port_declaration_head(self, items):
        if len(items) == 1:
            return items[0]
        else:
            port_header: Tree = items[0]
            port: Port = items[1]
            headerType = port_header.data

            if headerType == "header0":
                val0 = port_header.children[0].data
                port.setType(val0)
            elif headerType == "header1":
                val0 = PortDirection.fromString(port_header.children[0].data)
                port.setDirection(val0)
            else:
                val0 = PortDirection.fromString(port_header.children[0].data)
                val1 = port_header.children[1].data
                port.setDirection(val0)
                port.setType(val1)
            return port

    # extended_port: port_range variable_list
    @v_args(inline=True)
    def extended_port(self, range, ports: list):
        new_ports = []
        for port in ports:
            port.setRange(range)
            new_ports.append(port)
        return new_ports

    # extended_port: port_range variable_list
    @v_args(inline=True)
    def extended_port_head(self, range, name):
        port = Port(name=name)
        port.setRange(range)
        return port

    # port_header: type | port_direction type?
    @v_args(inline=False)
    def port_header(self, args):
        print(args)
        return None, None

    # simple_port: variable_list
    @v_args(inline=True)
    def simple_port(self, ports):
        return ports

    # simple_port: variable_name
    @v_args(inline=True)
    def simple_port_head(self, name):
        return Port(name=name)

    # port_list: "(" port_declaration ("," port_declaration)* ")"
    def port_list(self, items):
        # concat the list of ports
        return items

    # variable_list: CNAME ("," CNAME)*
    def variable_list(self, items):
        return [Port(name=item) for item in items]

    # port_range : "[" expression ":" expression "]"
    @v_args(inline=True)
    def port_range(self, start, end):
        assert isinstance(start, DFGNode)
        assert isinstance(end, DFGNode)
        return Range(start, end)
