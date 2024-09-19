#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-25 14:49:54
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-25 15:24:24
"""


class ModuleParameters:
    def __init__(self) -> None:
        self.module_name = None
        self.parameters = {}

    def addParameter(self, name: str, value: str):
        self.parameters[name] = value

    def getParameter(self, name: str):
        return self.parameters[name]

    def getParameters(self):
        return self.parameters

    def setModuleName(self, name: str):
        self.module_name = name

    def getInstName(self):
        return self.module_name
