#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 18:22:19
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 19:03:09
"""

from .dfg import *


class TimeValue:
    def __init__(self, value: int, unit: str) -> None:
        self.value = value
        self.unit = unit

    def __repr__(self) -> str:
        return f"{int(self.value)} {self.unit}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, TimeValue):
            print(f"Value {value} is not TimeValue")
            return False
        if self.value != value.value:
            print(f"Value {self.value} != {value.value}")
            return False
        if self.unit != value.unit:
            print(f"Unit {self.unit} != {value.unit}")
            return False
        return True


class Parameter:
    def __init__(self, range: Range, name: str, value: str):
        self.name = name
        self.range = range
        self.value = value

    def __repr__(self):
        return "#{}".format(self.name, self.value)

    def getName(self):
        return self.name


class ParameterHandler:
    def __init__(self):
        self.param_list = {}

    def addParameter(self, param: Parameter):
        self.param_list[param.getName()] = param

    def addParameters(self, parameters: list):
        if not parameters:
            return
        for parameter in parameters:
            self.addParameter(parameter)

    def getParameter(self, name: str):
        return self.param_list[name]

    def getParameters(self):
        return self.param_list

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, ParameterHandler):
            return False
        for key, param in self.param_list.items():
            if key not in value.getParameters():
                return False
            if value.getParameter(key) != param:
                return False
        return True


class Macros(dict):
    def __init__(self):
        super().__init__()

    def addMacro(self, name: str, value: str):
        self[name] = value

    def getMacros(self):
        return self

    def getMacroString(self):
        retString = ""
        for key, value in self.items():
            retString += f"`define {key} {value}\n"
        return retString

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Macros):
            return False
        for key, macro in self.items():
            if key not in value.getMacros():
                return False
            if value.getMacros()[key] != macro:
                return False
        return True


class TimeScale:
    def __init__(self):
        self.val1: TimeValue = None
        self.val2: TimeValue = None

    def setTimescale(self, val1: TimeValue, val2: TimeValue):
        self.val1 = val1
        self.val2 = val2

    def getTimescaleString(self):
        if self.val1 is None or self.val2 is None:
            return ""
        return f"`timescale {self.val1} / {self.val2}\n"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, TimeScale):
            return False
        if self.val1 != value.val1:
            return False
        if self.val2 != value.val2:
            return False
        return True
