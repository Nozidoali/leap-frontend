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
        t = (
            PortType.fromString(t.data) if t is not None else None
        )  # NOTE: by default, the type is None to avoid overwriting failure
        port = Port(name)
        port.setAll(dir, t, range)
        return port

    def blocking_assignment(self, items):
        return BlockingAssignment(items[0], items[1])

    def non_blocking_assignment(self, items):
        return NonBlockingAssignment(items[0], items[1])

    # module_instantiation: CNAME parameter_instance? CNAME "(" module_instance_arguments ")" ";"
    def module_instantiation(self, items) -> Statement:
        module_name, parameter_list, instance_name, argument_list = items
        inst: ModuleInst = ModuleInst(instance_name, module_name)
        inst.addParameters(parameter_list)
        inst.setAssignments(argument_list)
        return ModuleInstantiation(inst)

    def argument_list(self, items):
        return items

    def named_argument(self, items):
        varname, expression = items
        return str(varname), expression

    def positional_argument(self, items):
        # TODO: implement this
        raise NotImplementedError()
        return None, items[0]

    def define_parameter(self, items):
        # usually, this block comes after the module instantiation
        return ModuleInstParameterDefinition(items)

    def parameter_definition(self, items):
        return items
