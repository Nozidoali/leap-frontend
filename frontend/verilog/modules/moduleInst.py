#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-25 14:55:16
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-25 15:59:34
"""


class ModuleInst:
    def __init__(self, name: str) -> None:
        self.name = name
        self.module_name = None
        self.port_list = []
        self.port_names = {}
        self.inplace_parameters = None
        self.parameter_list = {}

        # self.port_index: int = 0
        self.is_standard_inst = True

    def addPort(self, name: str, value: str):
        self.port_list.append(value)
        index = len(self.port_list) - 1
        if name is None:
            name = f"port_{index}"
            self.is_standard_inst = False
        self.port_names[name] = index

    def getPort(self, name: str):
        index = self.port_names[name]
        return self.port_list[index]

    def getPorts(self):
        return self.port_list

    def addParameter(self, name: str, value: str):
        self.parameter_list[name] = value

    def setModuleName(self, name: str):
        self.module_name = name

    def setInplaceParameters(self, inplace_parameters):
        self.inplace_parameters = inplace_parameters[:]

    def getInplaceParameters(self):
        return self.inplace_parameters

    def hasInplaceParameters(self):
        return self.inplace_parameters is not None

    def getInstName(self):
        return self.name

    def getModuleName(self):
        return self.module_name

    def getPortList(self):
        return self.port_names.keys()

    def getParameters(self):
        return self.parameter_list

    def hasParameters(self):
        return len(self.parameter_list) > 0
