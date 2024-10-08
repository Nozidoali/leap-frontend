import pygraphviz as pgv

from ...modules import *


class CFGraph(pgv.AGraph):

    def getLatency(self, node: pgv.Node):
        return int(node.attr["latency"])

    def getII(self, node: pgv.Node):
        if "II" not in node.attr:
            return None
        if node.attr["II"] == "None":
            return None
        return node.attr["II"]

    def addBB(
        self,
        name: str,
        latency: int,
        II: int = None,
        isStart: bool = False,
        isFinish: bool = False,
    ):
        self.add_node(
            name,
            shape="box",
            latency=latency,
            II=II,
            isStart="true" if isStart else "false",
            isFinish="true" if isFinish else "false",
        )

    def addFlow(self, src: str, dst: str):
        self.add_edge(src, dst)

    @staticmethod
    def isStart(node: pgv.Node):
        return node.attr["isStart"] == "true"

    @staticmethod
    def isFinish(node: pgv.Node):
        return node.attr["isFinish"] == "true"
