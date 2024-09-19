from .node import *


class ConstantNode(DFGNode):
    def __init__(self, value: int):
        super().__init__(str(value))
        self.operation = SOPType.CONST

    @property
    def needsParentheses(self):
        return False
