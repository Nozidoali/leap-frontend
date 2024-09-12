#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 14:17:13
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 14:20:37
"""

from typing import List, Dict
from .verilogUtils import ContinuousAssign
from .verilogNumber import Range


class ModuleInstance:
    def __init__(self, module_name: str, instance_name: str, ports: Dict[str, str]):
        self.module_name = module_name
        self.instance_name = instance_name
        self.ports = ports

    def __repr__(self):
        return "ModuleInstance({}, {}, {})".format(
            self.module_name, self.instance_name, self.ports
        )


class NetDeclaration:
    def __init__(self, net_name: str, range: Range):
        self.net_name = net_name
        self.range = range

    def __repr__(self):
        if self.range is not None:
            return "NetDeclaration({} {})".format(self.net_name, self.range)
        else:
            return "NetDeclaration({})".format(self.net_name)


class OutputDeclaration(NetDeclaration):
    def __repr__(self):
        if self.range is not None:
            return "OutputDeclaration({} {})".format(self.net_name, self.range)
        else:
            return "OutputDeclaration({})".format(self.net_name)


class InputDeclaration(NetDeclaration):
    def __repr__(self):
        if self.range is not None:
            return "InputDeclaration({} {})".format(self.net_name, self.range)
        else:
            return "InputDeclaration({})".format(self.net_name)


class Module:
    def __init__(self, module_name: str, port_list: List[str], module_items: List):
        self.module_name = module_name
        self.port_list = port_list

        self.module_items = module_items

        self.net_declarations = []
        self.output_declarations = []
        self.input_declarations = []
        self.module_instances = []
        self.assignments = []
        self.sub_modules = []

        for it in module_items:
            if isinstance(it, OutputDeclaration):
                self.output_declarations.append(it)
            elif isinstance(it, InputDeclaration):
                self.input_declarations.append(it)
            elif isinstance(it, NetDeclaration):
                self.net_declarations.append(it)
            elif isinstance(it, ModuleInstance):
                self.module_instances.append(it)
            elif isinstance(it, ContinuousAssign):
                self.assignments.append(it)
            elif isinstance(it, Module):
                self.sub_modules.append(it)

    def __repr__(self):
        return "Module({}, {}, {})".format(
            self.module_name, self.port_list, self.module_items
        )


class Netlist:
    def __init__(self, modules: List[Module]):
        self.modules = modules

    def __repr__(self):
        return "Netlist({})".format(self.modules)
