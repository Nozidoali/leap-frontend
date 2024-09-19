from .node import *
from .range import *


class VariableNode(DFGNode):
    def __init__(self, variable_name: str):
        if isinstance(variable_name, VariableNode):
            variable_name = variable_name.variable_name
        super().__init__(variable_name)
        self.operation = SOPType.VARIABLE

    @property
    def needsParentheses(self):
        return False

    def toString(self) -> str:
        return (
            self.variable_name
            if self.range is None
            else f"{self.variable_name}{rangeToString(self.range)}"
        )
