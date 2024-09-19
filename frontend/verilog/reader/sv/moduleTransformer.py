#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 23:18:52
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-26 00:00:10
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args
from ...modules import *

class ModuleTransformer(Transformer):
    # this is a list of lots of items, so we set inline=False
    # module: "module" CNAME module_definition ";" declaration* "endmodule"
    @v_args(inline=False)
    def module(self, items):
        module_definition = items[0]
        module_name, param_list, port_list = module_definition

        module_items = items[1:]
        module = Module()
        module.setName(module_name)
        module.addPorts(port_list)
        module.addParameters(param_list)
        module.load(module_items)
        
        return module

    @v_args(inline=False)
    def module_definition(self, args):
        module_name = str(args[0])
        param_list = []
        port_list = []
        for item in args[1:]:
            if not isinstance(item, list):
                continue

            if len(item) > 0 and isinstance(item[0], Port):
                port_list.extend(item)
            elif len(item) > 0 and isinstance(item[0], Parameter):
                param_list.extend(item)
            else:
                assert False, f"item = {item}"
        return module_name, param_list, port_list

    @v_args(inline=True)
    def parameter_declaration(self, type, lvalue, expression):
        """
        parameter_declaration: ["signed"] [range] lvalue "=" expression
        """
        return Parameter(range=range, name=lvalue, value=expression)

    # parameter_assignment: parameter_type port_range? CNAME "=" parameter_value ";"
    # parameter_value: NUMBER based_number | NUMBER
    def parameter_assignment(self, items):
        parameterType = items[0]
        if len(items) == 4:
            range = items[1]
            name = items[2]
            value = items[3]
        else:
            range = None
            name = items[1]
            value = items[2]
        return "parameter_assignment", Parameter(range, name, value)

    def parameter_value(self, items):
        return items[0]

    @v_args(inline=True)
    def variable_assignment(self, signal, type, expression):
        if isinstance(signal, DFGNode):
            pass
        elif isinstance(signal, str):
            signal = VariableNode(signal)
        else:
            raise ValueError(f"signal = {signal}")

        assert isinstance(expression, DFGNode), f"expression = {expression}"
        assignment = Assignment(signal, expression)
        assignmentType = type.data
        assignment.setType(assignmentType)
        return "variable_assignment", assignment

    def system_task(self, items):
        return "system_task", []

    # module_instantiation: CNAME parameter_instance? CNAME "(" module_instance_arguments ")" ";"
    def module_instantiation(self, items):

        if len(items) == 3:
            module_name = items[0]
            parameter_list = None
            module_inst_name = items[1]
            pin_list = items[2]
        elif len(items) == 4:
            module_name = items[0]
            parameter_list = items[1]
            module_inst_name = items[2]
            pin_list = items[3]

        inst = ModuleInst(module_inst_name)
        inst.setModuleName(module_name)
        if parameter_list is not None:
            inst.setInplaceParameters(parameter_list)

        for key, value in pin_list:
            inst.addPort(key, value)

        return "module_instantiation", inst

    def parameter_instance(self, items):
        return items[0]

    def parameter_instance_arguments(self, items):
        return items

    def module_instance_arguments(self, items):
        return items

    def standard_module_instance_argument(self, items):
        pin_name = items[0]
        pin_signal = items[1] if len(items) > 1 else None
        return pin_name, pin_signal

    def short_module_instance_argument(self, items):
        pin_name = None
        pin_signal = items[0]
        return pin_name, pin_signal

    def define_parameter(self, items):
        # usually, this block comes after the module instantiation
        moduleParameter = ModuleParameters()
        for item in items[0]:
            module_name, parameter_name, expression = item
            if moduleParameter.module_name is None:
                moduleParameter.setModuleName(module_name)
            assert (
                moduleParameter.module_name == module_name
            ), f"module_name = {module_name}"
            moduleParameter.addParameter(parameter_name, expression)
        return "define_parameter", moduleParameter

    def parameter_definitions(self, items):
        return items

    def parameter_definition(self, items):
        module_parameter = items[0]
        expression = items[1]

        assert "." in module_parameter, f"module_parameter = {module_parameter}"
        module_name, parameter_name = module_parameter.split(".")
        return module_name, parameter_name, expression

    def module_parameter(self, items):
        module_name = items[0]
        parameter_name = items[1]
        return f"{module_name}.{parameter_name}"

    @v_args(inline=True)
    def variable_name(self, name):
        return str(name)
