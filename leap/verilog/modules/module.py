#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 18:07:25
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:55:15
"""

from .dfg import *
from .assignment import *
from .moduleInst import *
from .moduleParameters import *
from .ports import *
from .parameters import *
from .bng import *

from enum import Enum

"""
// 1.4 Module. i.e., what is inside a module
?module_body: always_block
            | port_declaration ";" // This includes reg, wire, integer, real, time, realtime
            | parameter_assignment // This includes parameters and localparams
            | variable_assignment ";" // This includes assign
            | system_task
            | module_instantiation // This includes module instantiation
            | define_parameter // This includes defparam
"""

class ModuleBodyType(Enum):
    ALWAYS_BLOCK = ("always_block",)
    PORT_DECLARATION = ("port_declaration",)
    PARAMETER_ASSIGNMENT = ("parameter_assignment",)
    VARIABLE_ASSIGNMENT = ("variable_assignment",)
    SYSTEM_TASK = ("system_task",)
    MODULE_INSTANTIATION = ("module_instantiation",)
    DEFINE_PARAMETER = ("define_parameter",)

    @staticmethod
    def fromString(label: str):
        if label == "always_block":
            return ModuleBodyType.ALWAYS_BLOCK
        elif label == "port_declaration":
            return ModuleBodyType.PORT_DECLARATION
        elif label == "parameter_assignment":
            return ModuleBodyType.PARAMETER_ASSIGNMENT
        elif label == "variable_assignment":
            return ModuleBodyType.VARIABLE_ASSIGNMENT
        elif label == "system_task":
            return ModuleBodyType.SYSTEM_TASK
        elif label == "module_instantiation":
            return ModuleBodyType.MODULE_INSTANTIATION
        elif label == "define_parameter":
            return ModuleBodyType.DEFINE_PARAMETER
        else:
            assert False, f"Unsupported module body type: {label}"

def unzipItems(items: list):
    """
    Due to the structure of the AST, the items may not arrive in the same level / depth.
    """
    allItems = []
    for item in items:
        statements = []
        if isinstance(item, tuple):
            statements = [item]
        if isinstance(item, list):
            statements = []
            for subItem in item:
                if isinstance(subItem, tuple):
                    statements.append(subItem)
                else:
                    statements.extend(subItem)
        allItems.extend(statements)
    return allItems

class Module(PortHandler, ParameterHandler, BNGraph):
    def __init__(
        self,
        module_name: str,
    ):
        PortHandler.__init__(self)
        ParameterHandler.__init__(self)
        BNGraph.__init__(self)
        self.module_name = module_name

    def __repr__(self):
        return f"Module({self.module_name})"

    def getDFG(self):
        return self.dfg

    def load(self, module_items: list):
        # load the DFG
        self.dfg = DFGraph()
        self.node_is_blocking = {}
        self.submodules = {}
        
        for statement in unzipItems(module_items):
            bodyType = ModuleBodyType.fromString(statement[0])
            match bodyType:
                case ModuleBodyType.PORT_DECLARATION:
                    self.addPorts(statement[1])
                case ModuleBodyType.VARIABLE_ASSIGNMENT:
                    self.addAssignment(statement[1])
                    # assignment = statement[1]

                    # newNodes = createAssignNodes(
                    #     assignment.expression,
                    #     assignment.target,
                    #     assignment.condition,
                    # )
                    # for node in newNodes:
                    #     nodeIndex = self.dfg.insertNode(node)
                    #     dfgNode = self.getNodeAtIndex(nodeIndex)
                    #     if dfgNode.isVariable:
                    #         self.node_is_blocking[dfgNode.label] = (
                    #             assignment.isBlocking
                    #         )

                case ModuleBodyType.PARAMETER_ASSIGNMENT:
                    self.addParameter(statement[1])

                case ModuleBodyType.MODULE_INSTANTIATION:
                    self.submodules[statement[1].getInstName()] = statement[1]

                case ModuleBodyType.DEFINE_PARAMETER:
                    moduleParameter: ModuleParameters = statement[1]
                    moduleInstName = moduleParameter.getInstName()
                    moduleInst: Module = self.submodules[moduleInstName]
                    parameters: dict = moduleParameter.getParameters()
                    moduleInst.addParameters(parameters)

                case ModuleBodyType.SYSTEM_TASK:
                    pass

                case _:
                    assert False, f"Unsupported module body type: {bodyType}"

    def getNodeAtIndex(self, index: int) -> DFGNode:
        return self.dfg.getNode(index)

    def getName(self):
        return self.module_name
