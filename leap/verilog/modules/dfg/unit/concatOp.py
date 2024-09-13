from .node import *
from typing import List

class ConcatOpNode(DFGNode):
    def __init__(self, children: List[DFGNode]):
        super().__init__("\{\}")
        self.children = children[:]

    def toString(self) -> str:
        return (
            "{"
            + ", ".join([child.toString() for child in self.children])
            + "}"
        )