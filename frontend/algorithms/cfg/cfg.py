import pygraphviz as pgv
from typing import List, Dict

from ...modules import *


class CFGraph(pgv.AGraph):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.graph_attr["rankdir"] = "TB"

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

    def addFlow(
        self,
        src: str,
        dst: str,
        isLoop: bool = False,
        loopBound: int = -1,
        loopII: int = -1,
    ):
        self.add_edge(
            src,
            dst,
            isLoop="true" if isLoop else "false",
            loopBound=loopBound,
            loopII=loopII,
        )

    @staticmethod
    def isStart(node: pgv.Node):
        return node.attr["isStart"] == "true"

    @staticmethod
    def isFinish(node: pgv.Node):
        return node.attr["isFinish"] == "true"

    @staticmethod
    def isLoop(edge: pgv.Edge):
        return edge.attr["isLoop"] == "true"

    @staticmethod
    def getLoopBound(edge: pgv.Edge):
        return int(edge.attr["loopBound"])

    @staticmethod
    def getLoopII(edge: pgv.Edge):
        return int(edge.attr["loopII"])
