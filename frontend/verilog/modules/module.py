#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 18:07:25
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:55:15
"""

from .dfg import *
from .moduleInst import *
from .ports import *
from .parameters import *

from enum import Enum


class Module(Frame, ParameterHandler, ExtendedGraph):
    def __init__(
        self,
    ):
        Frame.__init__(self)
        ParameterHandler.__init__(self)
        BNGraph.__init__(self)
        self.setName("top")
        self.submodules = {}
        self.macros = {}

    def addMacro(self, name: str, macro: Any):
        self.macros[name] = macro

    def addInstance(self, inst: ModuleInst):
        self.submodules[inst.getName()] = inst

    def setName(self, module_name: str):
        self.module_name = module_name

    def __repr__(self):
        return f"Module({self.module_name})"

    def loadModuleItems(self, module_items: list):
        # loadModuleItems the DFG
        self.node_is_blocking = {}
        self.submodules = {}
        for item in module_items:
            print(item)

    def getName(self):
        return self.module_name

    def getGraph(self, skipConstants=True) -> pgv.AGraph:
        DotGraph.exportDOT(self, params={"skipConstants": skipConstants})
        return self.graph

    def separateCDFG(self, DFG: pgv.AGraph, CFG: pgv.AGraph):
        fsmGraph = self.graph.add_subgraph(
            DFG,
            name="cluster_data_flow",
            label="DATA_FLOW",
            style="dashed",
            color="blue",
        )
        fsmGraph.graph_attr["rankdir"] = "LR"  # Left-to-right layout

        for node in DFG.nodes():
            self._highlightNode(node, "CYAN")
