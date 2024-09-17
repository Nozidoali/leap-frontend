#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 18:22:19
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 19:03:09
"""

import logging

logger = logging.getLogger(__name__)

from .dfg import *


class Parameter:
    def __init__(self, range: Range, name: str, value: str):
        logger.info(f"Parameter: {name} = {value}")
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
        for parameter in parameters:
            self.addParameter(parameter)
    
    def getParameter(self, name: str):
        return self.param_list[name]
    
    def getParameters(self):
        return self.param_list