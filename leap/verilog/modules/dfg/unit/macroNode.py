from .node import *

class MacroNode(DFGNode):
    def __init__(self, child: DFGNode):
        super().__init__("`")
        self.operation = UOPType.MACRO
        self.children = [child]
