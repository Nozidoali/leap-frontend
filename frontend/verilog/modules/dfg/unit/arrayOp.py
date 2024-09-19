from .node import *
from .variableNode import *


class ArrayOpNode(VariableNode):
    def __init__(self, variable_name: str, start: int, end: int = None):
        super().__init__(variable_name)
        self.range = Range(start, end) if end is not None else Range(start)

    def toString(self) -> str:
        return f"{self.variable_name}{rangeToString(self.range)}"
