from .node import *
from typing import List


class FuncNode(DFGNode):
    def __init__(self, func_name: str, children: List[DFGNode]):
        super().__init__(func_name)
        self.operation = SOPType.FUNCTION
        self.children = children[:]

    def toString(self) -> str:
        return (
            f"${self.variable_name}("
            + ", ".join([child.toString() for child in self.children])
            + ")"
        )
