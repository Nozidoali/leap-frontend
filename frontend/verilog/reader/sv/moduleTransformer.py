#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 23:18:52
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-26 00:00:10
"""

from lark import Transformer
from ...modules import *
from .larkUtils import *


class ModuleTransformer(Transformer):

    def netlist(self, items):
        return Netlist(items)

    # this is a list of lots of items, so we set inline=False
    # module: "module" CNAME module_definition ";" declaration* "endmodule"
    def module(self, items):
        name, param_list, port_list = items[:3]
        module: Module = Module()
        module.setName(str(name))
        module.addParameters(param_list)
        module.addPorts(port_list)
        [x(module) for x in flatten(items[3:])]
        return module

    def parameter_list(self, items):
        items = flatten(items)
        return items

    def port_list(self, items):
        items = flatten(items)
        return items

    def port_definition(self, items):
        dir, t, range, name = items
        dir = PortDirection.fromString(dir.data) if dir is not None else None
        t = PortType.fromString(t.data) if t is not None else None
        port = Port(name)
        port.setAll(dir, t, range)
        return port

    def blocking_assignment(self, items):
        return BlockingAssignment(items[0], items[1])

    def non_blocking_assignment(self, items):
        return NonBlockingAssignment(items[0], items[1])

    # module_instantiation: CNAME parameter_instance? CNAME "(" module_instance_arguments ")" ";"
    def module_instantiation(self, items) -> Statement:
        parameter_list = None
        if len(items) == 3:
            module_name, module_inst_name, pin_list = items
        elif len(items) == 4:
            module_name, parameter_list, module_inst_name, pin_list = items
        inst = ModuleInst(module_inst_name)
        inst.setModuleName(module_name)
        if parameter_list is not None:
            inst.setInplaceParameters(parameter_list)
        for key, value in pin_list:
            inst.addPort(key, value)
        return ModuleInstantiation(inst)

    def define_parameter(self, items):
        # usually, this block comes after the module instantiation
        return items
