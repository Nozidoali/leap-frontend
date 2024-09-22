from frontend.verilog.modules.dfg import Any
from frontend.verilog.modules.module import Any, Module
from .dfg import *
from .module import *
from .moduleInst import *


class Statement:
    def __init__(self) -> None:
        self.condition: DFGNode = None
        self.event: DFGNode = None

    def setCondition(self, condition):
        self.condition = condition

    def addCondition(self, condition: DFGNode):
        if condition is None:
            return
        if self.condition is None:
            self.condition = condition
        else:
            self.condition = OPNode("&&", OPType.BINARY_AND, self.condition, condition)
        return self

    def setEvent(self, event: DFGNode):
        self.event = event
        return self

    def __call__(self, module: Module) -> Any:
        raise NotImplementedError


class ModuleInstantiation(Statement):
    def __init__(self, inst: ModuleInst) -> None:
        super().__init__()
        self.inst = inst

    def __call__(self, module: Module) -> Any:
        module.addInstance(self.inst)

    def __repr__(self) -> str:
        return f"ModuleInstantiation({self.inst})"


class PortDeclaration(Statement):
    def __init__(self, ports: list) -> None:
        super().__init__()
        self.ports = ports

    def __repr__(self) -> str:
        return f"PortDeclaration({self.ports})"

    def __call__(self, module: Module) -> Any:
        module.addPorts(self.ports)


class MacroDefinition(Statement):
    def __init__(self, name: str, value: DFGNode) -> None:
        super().__init__()
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f"MacroDefinition({self.name} = {self.value})"

    def __call__(self, module: Module) -> Any:
        module.addMacro(self.name, self.value)


class Assignment(Statement):
    def __init__(
        self, target: DFGNode, expression: DFGNode, condition: DFGNode = None
    ) -> None:
        self.target: DFGNode = target
        self.expression: DFGNode = expression
        self.condition: DFGNode = condition
        self.type = None
        self.isBlocking = False

    def __repr__(self) -> str:
        retString = ""
        if self.isBlocking:
            retString += f"{self.target} = {self.expression}"
        else:
            retString += f"{self.target} <= {self.expression} ({self.condition})"
        return retString

    def replaceVariable(self, old: str, new: str):
        self.target.replaceVariable(old, new)
        self.expression.replaceVariable(old, new)
        if self.condition is not None:
            self.condition.replaceVariable(old, new)

    def __call__(self, module: Module) -> Any:
        return module.addAssignment(self)


class BlockingAssignment(Assignment):
    def __init__(
        self, target: DFGNode, expression: DFGNode, condition: DFGNode = None
    ) -> None:
        super().__init__(target, expression, condition)
        self.isBlocking = True


class NonBlockingAssignment(Assignment):
    def __init__(
        self, target: DFGNode, expression: DFGNode, condition: DFGNode = None
    ) -> None:
        super().__init__(target, expression, condition)
        self.isBlocking = False
