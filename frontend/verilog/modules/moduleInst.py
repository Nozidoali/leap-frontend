#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-25 14:55:16
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-25 15:59:34
"""


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
