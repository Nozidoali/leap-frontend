from ...modules import *
from ..cfg import *


class ModuleGenerator:

    def __init__(self) -> None:
        self.module = Module()

    def getModule(self) -> Module:
        return self.module

    def run(self) -> None:
        raise NotImplementedError()

    def createReg(self, name: str, width: int = 1) -> BNode:
        reg = VarNode(name)
        self.module.addPort(RegPort(reg, BasicRange(width)))
        return reg

    def createWire(self, name: str, width: int = 1) -> BNode:
        wire = VarNode(name)
        self.module.addPort(WirePort(wire, BasicRange(width)))
        return wire

    def addAssignment(self, assignment: BNEdge) -> None:
        self.module.addAssignment(assignment)
