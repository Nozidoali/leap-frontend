#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 18:07:25
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:55:15
"""

from typing import List, Dict

from .dfg import *
from .frame import *
from .definitions import *


class ModuleInst:
    def __init__(self, instName: str, moduleName: str) -> None:
        self.instName: str = instName
        self.moduleName: str = moduleName
        self.assignment_list: List[Assignment] = []
        self.parameter_list: Dict[str, str] = {}

    def setAssignments(self, assignments: List[Assignment]) -> None:
        if not assignments:
            return
        self.assignment_list = assignments

    def addParameters(self, parameters: Dict[str, str]) -> None:
        if not parameters:
            return
        self.parameter_list.update(parameters)

    def addParameter(self, paramName: str, paramValue: str) -> None:
        self.parameter_list[paramName] = paramValue

    def getParameters(self) -> Dict[str, str]:
        return self.parameter_list

    def getAssignments(self) -> List[Assignment]:
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
        self.submodules: Dict[str, ModuleInst] = {}
        self.node2assignment = {}
        self.setName("top")

    def addInstance(self, inst: ModuleInst):
        self.submodules[inst.name] = inst

    def addParameterToModuleInst(self, instName: str, paramName: str, paramValue: str):
        if instName not in self.submodules:
            print(f"Instance {instName} not found in {self.getName()}")
            return
        inst = self.submodules[instName]
        inst.addParameter(paramName, paramValue)

    def setName(self, module_name: str) -> None:
        self.module_name = module_name

    def getName(self) -> str:
        return self.module_name

    @property
    def hasInstances(self) -> bool:
        return len(self.submodules) > 0

    def __repr__(self) -> str:
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

    def postProcess(self, params: dict = {}) -> None:
        # sanity check on the assignments
        for assignment in self.getAssignments():
            if assignment.target.name not in self.getPortNames():
                raise ValueError(
                    f"Assignment target {assignment.target.name} not found in module {self.getName()}"
                )
            port = self.getPort(assignment.target.name)
            assignment.targetType = port.getType()

        # turn submodules into assignments
        if self.hasInstances:
            # just skip it for now
            return

        # check the definitions
        for port in self.getPortNames():
            if self.isDefined(port) and self.getPort(port).isPi:
                raise ValueError(
                    f"Input port {port} is assigned in module {self.getName()}"
                )
            if not self.isDefined(port) and self.getPort(port).isPo:
                raise ValueError(
                    f"Output port {port} is not assigned in module {self.getName()}"
                )
