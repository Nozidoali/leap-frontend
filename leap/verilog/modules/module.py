#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 18:07:25
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:55:15
"""

from .dfg import *
from .assignment import *
from .moduleInst import *
from .moduleParameters import *
from .ports import *
from .parameters import *

from enum import Enum

"""
// 1.4 Module. i.e., what is inside a module
?module_body: always_block
            | port_declaration ";" // This includes reg, wire, integer, real, time, realtime
            | parameter_assignment // This includes parameters and localparams
            | variable_assignment ";" // This includes assign
            | system_task
            | module_instantiation // This includes module instantiation
            | define_parameter // This includes defparam
"""


class ModuleBodyType(Enum):
    ALWAYS_BLOCK = ("always_block",)
    PORT_DECLARATION = ("port_declaration",)
    PARAMETER_ASSIGNMENT = ("parameter_assignment",)
    VARIABLE_ASSIGNMENT = ("variable_assignment",)
    SYSTEM_TASK = ("system_task",)
    MODULE_INSTANTIATION = ("module_instantiation",)
    DEFINE_PARAMETER = ("define_parameter",)

    @staticmethod
    def fromString(label: str):
        if label == "always_block":
            return ModuleBodyType.ALWAYS_BLOCK
        elif label == "port_declaration":
            return ModuleBodyType.PORT_DECLARATION
        elif label == "parameter_assignment":
            return ModuleBodyType.PARAMETER_ASSIGNMENT
        elif label == "variable_assignment":
            return ModuleBodyType.VARIABLE_ASSIGNMENT
        elif label == "system_task":
            return ModuleBodyType.SYSTEM_TASK
        elif label == "module_instantiation":
            return ModuleBodyType.MODULE_INSTANTIATION
        elif label == "define_parameter":
            return ModuleBodyType.DEFINE_PARAMETER
        else:
            assert False, f"Unsupported module body type: {label}"

class Module(PortHandler, ParameterHandler):
    def __init__(
        self,
        module_name: str,
    ):
        PortHandler.__init__(self)
        ParameterHandler.__init__(self)
        self.module_name = module_name

    def __repr__(self):
        return f"Module({self.module_name})"

    def getDFG(self):
        return self.dfg

    def load(self, module_items: list):
        # load the DFG
        self.dfg = DFGraph()
        self.node_is_blocking = {}
        self.submodules = {}
        for item in module_items:
            statements = []
            if isinstance(item, tuple):
                statements = [item]
            if isinstance(item, list):
                statements = []
                for subItem in item:
                    if isinstance(subItem, tuple):
                        statements.append(subItem)
                    else:
                        statements.extend(subItem)
            for statement in statements:
                assert isinstance(statement, tuple), f"statement = {statement}"
                bodyType = ModuleBodyType.fromString(statement[0])
                match bodyType:
                    case ModuleBodyType.PORT_DECLARATION:
                        ports = statement[1]
                        self.addPorts(ports)
                    case ModuleBodyType.VARIABLE_ASSIGNMENT:
                        assignment = statement[1]
                        # print(assignment)

                        lhs: DFGNode = assignment.target
                        rhs: DFGNode = assignment.expression
                        # assert rhs.isVariable(), f"rhs = {rhs}"
                        # assert lhs.isVariable(), f"lhs = {lhs}"

                        newNodes = createAssignNodes(
                            assignment.expression,
                            assignment.target,
                            assignment.condition,
                        )
                        for node in newNodes:
                            nodeIndex = self.dfg.insertNode(node)
                            dfgNode = self.getNodeAtIndex(nodeIndex)
                            if dfgNode.isVariable:
                                # print(
                                #     f"Node: {nodeIndex}, label: {dfgNode.label}, isBlocking: {assignment.isBlocking}"
                                # )
                                self.node_is_blocking[dfgNode.label] = (
                                    assignment.isBlocking
                                )

                    case ModuleBodyType.PARAMETER_ASSIGNMENT:
                        parameter = statement[1]
                        self.param_list[parameter.getName()] = parameter

                    case ModuleBodyType.MODULE_INSTANTIATION:
                        moduleInst = statement[1]
                        assert isinstance(
                            moduleInst, ModuleInst
                        ), f"moduleInst = {moduleInst}"
                        self.submodules[moduleInst.getInstName()] = moduleInst

                    case ModuleBodyType.DEFINE_PARAMETER:
                        moduleParameter: ModuleParameters = statement[1]

                        moduleInstName = moduleParameter.getInstName()
                        assert (
                            moduleInstName in self.submodules
                        ), f"moduleInstName = {moduleInstName}, available = {self.submodules.keys()}"

                        moduleInst = self.submodules[moduleInstName]

                        parameters: dict = moduleParameter.getParameters()

                        for key, value in parameters.items():
                            moduleInst.addParameter(key, value)

                    case ModuleBodyType.SYSTEM_TASK:
                        pass

                    case _:
                        assert False, f"Unsupported module body type: {bodyType}"
                        raise NotImplementedError

    def getNodeAtIndex(self, index: int) -> DFGNode:
        return self.dfg.getNode(index)

    def getName(self):
        return self.module_name

    def getInternalSignalList(self):
        return list(self.internal_signals.keys())