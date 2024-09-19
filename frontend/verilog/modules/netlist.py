#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 17:11:35
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 22:59:35
"""

from .module import Module


class Netlist:
    def __init__(self, modules: list, definitions: dict = {}):
        self.modules = modules[:]

        assert isinstance(definitions, dict), "definitions should be a dict"
        self.definitions = definitions.copy()

    def __repr__(self):
        return "Netlist({})".format(self.modules)

    def getModule(self, name: str) -> Module:
        for module in self.modules:
            if module.module_name == name:
                return module
        return None

    def getModules(self) -> list:
        moduleNames = []
        for module in self.modules:
            moduleNames.append(module.module_name)
        return moduleNames

    def getDefinitions(self) -> dict:
        return self.definitions
