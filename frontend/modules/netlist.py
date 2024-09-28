#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 17:11:35
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 22:59:35
"""

from typing import List
from .module import Module
from .definitions import *


class Netlist(Macros, TimeScale):
    """
    A netlist is a collection of modules
    """

    def __init__(self):
        Macros.__init__(self)
        TimeScale.__init__(self)
        self.modules = {}

    def addModule(self, module: Module):
        self.modules[module.getName()] = module

    def __repr__(self):
        return "Netlist({})".format(self.modules)

    def getModule(self, name: str) -> Module:
        return self.modules.get(name, None)

    def getModuleNames(self) -> List[str]:
        return list(self.modules.keys())

    def getModules(self) -> List[Module]:
        return list(self.modules.values())

    def getModuleAt(self, index: int) -> Module:
        # Especially useful for netlist with only one module
        return self.getModule(self.getModuleNames()[index])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Netlist):
            return False
        if len(self.getModuleNames()) != len(other.getModuleNames()):
            print(
                f"Number of modules are not equal: {len(self.getModuleNames())} != {len(other.getModuleNames())}"
            )
            return False
        # compare modules
        for module in self.getModuleNames():
            if module not in other.getModuleNames():
                print(f"Module {module} not found in other")
                print(f"Modules in self: {self.getModuleNames()}")
                print(f"Modules in other: {other.getModuleNames()}")
                return False
            if self.getModule(module) != other.getModule(module):
                print(
                    f"Module {module} in self is not equal to module {module} in other"
                )
                return False

        # compare parameters
        return super().__eq__(other)

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
