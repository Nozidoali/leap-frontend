from .node import *


class UnaryOpNode(DFGNode):
    def __init__(self, op: UOPType, child: DFGNode):
        op = op if isinstance(op, UOPType) else UOPType.fromString(op)
        super().__init__(str(op.value))
        self.operation = op
        self.children = [child]

    @property
    def needsParentheses(self):
        if self.operation == UOPType.MACRO:
            return False
        return True

    def toString(self) -> str:
        childStr = self.children[0].toString()
        if self.children[0].needsParentheses:
            childStr = f"({childStr})"
        return f"{self.variable_name}({childStr})"
