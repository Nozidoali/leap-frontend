#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 18:22:19
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 19:03:09
"""

from typing import Optional
from dataclasses import dataclass
from .dfg import *


@dataclass
class TimeValue:
    value: int
    unit: str

    def __repr__(self) -> str:
        return f"{int(self.value)} {self.unit}"


@dataclass
class Parameter:
    range: Range
    name: str
    value: BNode

    def __repr__(self) -> str:
        return f"#{self.name} {self.value.toString()}"

    def getName(self) -> str:
        return self.name


class ParameterHandler(dict):
    def addParameter(self, param: Parameter):
        self[param.getName()] = param

    def addParameters(self, parameters: list):
        if not parameters:
            return
        for parameter in parameters:
            self.addParameter(parameter)

    def getParameter(self, name: str):
        return self[name]

    def getParameters(self):
        return self


class Macros(dict):
    def addMacro(self, name: str, value: BNode):
        self[name] = value

    def getMacros(self):
        return self

    def getMacroString(self):
        retString = ""
        for key, value in self.items():
            retString += f"`define {key} {value.toString()}\n"
        return retString


@dataclass
class TimeScale:
    val1: Optional[TimeValue] = None
    val2: Optional[TimeValue] = None

    def setTimescale(self, val1: TimeValue, val2: TimeValue):
        self.val1 = val1
        self.val2 = val2

    def getTimescaleString(self) -> str:
        if self.val1 is None or self.val2 is None:
            return ""
        return f"`timescale {self.val1} / {self.val2}\n"
