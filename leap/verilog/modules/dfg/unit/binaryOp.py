from .node import *

class BinaryOpNode(DFGNode):
    def __init__(self, op: BOPType, left: DFGNode, right: DFGNode):
        op = op if isinstance(op, BOPType) else BOPType.fromString(op)
        super().__init__(str(op.value))
        self.operation = op
        self.children = [left, right]

    def toString(self) -> str:
        leftOp, rightOp = [f"({X.toString()})" if X.needsParentheses else f"{X.toString()}" for X in self.children]
        return f"{leftOp} {self.variable_name} {rightOp}"