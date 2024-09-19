from .node import *

class MuxNode(DFGNode):
    def __init__(self, cond: DFGNode, branch1: DFGNode, branch2: DFGNode):
        super().__init__("?")
        self.operation = SOPType.CONDITIONAL
        
        # TODO: treat cond as a single bit
        self.children = [cond, branch1, branch2]

    def toString(self) -> str:
        return f"({self.children[0].toString()}) ? {self.children[1].toString()} : {self.children[2].toString()}"