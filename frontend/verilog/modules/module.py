#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 18:07:25
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:55:15
"""

from .dfg import *
from .ports import *
from .definitions import *


class ModuleInst:
    def __init__(self, instName: str, moduleName: str) -> None:
        self.instName: str = instName
        self.moduleName: str = moduleName
        self.assignment_list: list = []
        self.parameter_list: dict = {}

    def setAssignments(self, assignments: list):
        if not assignments:
            return
        self.assignment_list = assignments

    def addParameters(self, parameters: dict):
        if not parameters:
            return
        self.parameter_list.update(parameters)

    def addParameter(self, paramName: str, paramValue: str):
        self.parameter_list[paramName] = paramValue

    def getParameters(self) -> dict:
        return self.parameter_list

    def getAssignments(self) -> list:
        return self.assignment_list

    @property
    def name(self) -> str:
        return self.instName

    @property
    def module(self) -> str:
        return self.moduleName


class Module(Frame, Macros, ParameterHandler, BNGraph):
    """
    Module class represents a module in a Verilog netlist.
    In LEAP, a module is:

    - A Frame, which is a collection of ports
    - A CDFG (BNGraph), which is the control/data flow graph of the module
    - A ParameterHandler, which describes the reconfigurable parameters of the module
    - A Macros, which contains the macros defined in the module (constant values)
    """

    def __init__(
        self,
    ):
        Frame.__init__(self)
        ParameterHandler.__init__(self)
        BNGraph.__init__(self)
        self.setName("top")
        self.submodules = {}
        self.macros = {}
        self.node2assignment = {}

    def addInstance(self, inst: ModuleInst):
        self.submodules[inst.name] = inst

    def addParameterToModuleInst(self, instName: str, paramName: str, paramValue: str):
        if instName not in self.submodules:
            print(f"Instance {instName} not found in {self.getName()}")
            return
        inst = self.submodules[instName]
        inst.addParameter(paramName, paramValue)

    def setName(self, module_name: str):
        self.module_name = module_name

    def getName(self):
        return self.module_name

    def __repr__(self):
        return f"Module({self.module_name})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Module):
            print(f"Type mismatch: {type(other)}")
            return False
        if self.getName() != other.getName():
            print(f"Module names are not equal: {self.getName()} != {other.getName()}")
            return False
        return (
            Frame.__eq__(self, other)
            and ParameterHandler.__eq__(self, other)
            and BNGraph.__eq__(self, other)
            and Macros.__eq__(self, other)
        )

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
