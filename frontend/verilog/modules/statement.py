from frontend.verilog.modules.dfg import Any
from frontend.verilog.modules.module import Any, Module
from .dfg import *
from .module import *
from .moduleInst import *
from .netlist import *
from .definitions import *


class Statement:
    """
    Statement is the base class for all statements in the module.
    It is a callable object that can be called with a module object to add the statement to the module.
    """

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

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Statement):
            print(f"Type mismatch: {type(value)}")
            return False
        if self.condition is None and value.condition is not None:
            print(f"Condition mismatch: {self.condition} != {value.condition}")
            return False
        if self.condition != value.condition:
            print(f"Condition mismatch: {self.condition} != {value.condition}")
            return False
        if self.event is None and value.event is not None:
            print(f"Event mismatch: {self.event} != {value.event}")
            return False
        if self.event != value.event:
            print(f"Event mismatch: {self.event} != {value.event}")
            return False
        return True


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
        self.name: DFGNode = name
        self.value: DFGNode = value

    def __repr__(self) -> str:
        return f"MacroDefinition({self.name} = {self.value.toString()})"

    def __call__(self, module: Module) -> Any:
        module.addMacro(self.name, self.value)


class TimeScaleDefinition(Statement):
    def __init__(self, val1: TimeValue, val2: TimeValue) -> None:
        super().__init__()
        self.val1 = val1
        self.val2 = val2

    def __repr__(self) -> str:
        return f"TimeScaleDefinition({self.val1} {self.val2})"

    def __call__(self, netlist: Netlist) -> Any:
        netlist.setTimescale(self.val1, self.val2)


class Assignment(Statement):
    def __init__(
        self, target: DFGNode, expression: DFGNode, condition: DFGNode = None
    ) -> None:
        super().__init__()
        self.target: DFGNode = target
        self.expression: DFGNode = expression
        self.type = None
        self.isBlocking = True

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

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Assignment):
            print(f"Type mismatch: {type(value)}")
            return False
        if self.target != value.target:
            print(f"Target mismatch: {self.target} != {value.target}")
            return False
        if self.expression != value.expression:
            print(f"Expression mismatch: {self.expression} != {value.expression}")
            return False
        if self.isBlocking != value.isBlocking:
            print(f"Blocking mismatch: {self.isBlocking} != {value.isBlocking}")
            return False
        return super().__eq__(value)


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
