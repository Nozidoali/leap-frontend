#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 23:59:53
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-24 01:11:59
"""

from .op import *
from .range import Range

class DFGNode:
    # Expressions are hard to handle because of the recursive nature

    def __init__(self, name: str = None) -> None:
        self.variable_name = name
        self.operation = None
        self.range = None
        self.children = []

    def __repr__(self) -> str:
        return self.toString()

    def isVariable(self):
        return self.operation == SOPType.VARIABLE

    def isConstant(self):
        return self.operation == SOPType.CONST

    def setRange(self, range: Range):
        self.range = range
        
    def toString(self) -> str:
        return self.variable_name

    @property
    def needsParentheses(self):
        return True