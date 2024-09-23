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
    """ 
    A netlist is a collection of modules
    
    :param modules: a list of modules
    :type modules: list
    :param definitions: a dictionary of definitions
    :type definitions: dict
    """
    def __init__(self, modules: list, definitions: dict = {}):
        self.modules = {m.getName(): m for m in modules}

        assert isinstance(definitions, dict), "definitions should be a dict"
        self.definitions = definitions.copy()

    def __repr__(self):
        return "Netlist({})".format(self.modules)

    def getModule(self, name: str) -> Module:
        return self.modules.get(name, None)

    def getModules(self) -> list:
        return list(self.modules.keys())

    def getDefinitions(self) -> dict:
        return self.definitions

    def getModuleAt(self, index: int) -> Module:
        # Especially useful for netlist with only one module
        return self.getModule(self.getModules()[index])
