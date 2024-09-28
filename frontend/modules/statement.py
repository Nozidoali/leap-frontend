from dataclasses import dataclass
from typing import List, Any
from abc import ABC, abstractmethod

from .dfg import *
from .module import *
from .netlist import *
from .definitions import *


class Statement(ABC):
    """
    Statement is the base class for all statements in the module.
    It is a callable object that can be called with a module object to add the statement to the module.
    """

    @abstractmethod
    def __call__(self, module: Module) -> Any:
        pass


class ModuleInstantiation(Statement):
    def __init__(self, inst: ModuleInst) -> None:
        super().__init__()
        self.inst = inst

    def __call__(self, module: Module) -> Any:
        module.addInstance(self.inst)

    def __repr__(self) -> str:
        return f"ModuleInstantiation({self.inst})"


class ModuleInstParameterDefinition(Statement):
    def __init__(self, parameters: list) -> None:
        super().__init__()
        self.parameters = parameters

    def __repr__(self) -> str:
        return f"ParameterDefinition({self.parameters})"

    def __call__(self, module: Module) -> Any:
        for instName, paramName, value in self.parameters:
            instName, paramName = str(instName), str(paramName)
            module.addParameterToModuleInst(instName, paramName, value)


@dataclass
class PortDeclaration(Statement):
    ports: List[Any]

    def __call__(self, module: Module) -> Any:
        module.addPorts(self.ports)


@dataclass
class MacroDefinition(Statement):
    name: str
    value: DFGNode

    def __call__(self, module: Module) -> Any:
        module.addMacro(self.name, self.value)

    def __repr__(self) -> str:
        return f"MacroDefinition({self.name} = {self.value.toString()})"


@dataclass
class TimeScaleDefinition(Statement):
    val1: TimeValue
    val2: TimeValue

    def __call__(self, netlist: Netlist) -> Any:
        netlist.setTimescale(self.val1, self.val2)

    def __repr__(self) -> str:
        return f"TimeScaleDefinition({self.val1} {self.val2})"


@dataclass
class AssignmentStatement(Statement):
    assignment: Assignment

    def __call__(self, module: Module) -> Any:
        module.addAssignment(self.assignment)

    def __repr__(self) -> str:
        return f"AssignmentStatement({self.assignment})"

    def addCondition(self, condition: DFGNode):
        self.assignment.addCondition(condition)
        return self

    def setEvent(self, event: DFGNode):
        self.assignment.setEvent(event)
        return self
