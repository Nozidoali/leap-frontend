import pygraphviz as pgv
from typing import List, Dict


class CFGraph(pgv.AGraph):

    def getLatency(self, node: pgv.Node):
        return int(node.attr["latency"])

    def getII(self, node: pgv.Node):
        if "II" not in node.attr:
            return None
        if node.attr["II"] == "None":
            return None
        return node.attr["II"]

    def addBB(self, name: str, latency: int, II: int = None):
        self.add_node(name, shape="box", latency=latency, II=II)

    def addFlow(self, src: str, dst: str):
        self.add_edge(src, dst)


class FSM(pgv.AGraph):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.graph_attr["rankdir"] = "TB"
        self.nodeToBB: Dict[str, str] = {}
        self.bbToNodes: Dict[str, List[str]] = {}

    def addBB(self, bb: pgv.Node):
        bbName = bb.name
        self.bbToNodes[bbName] = []
        latency = int(bb.attr["latency"])

        prevNode = None
        for i in range(latency):
            nodeName = f"s{len(self.nodes())}"
            self.add_node(nodeName)
            self.nodeToBB[nodeName] = bbName
            self.bbToNodes[bbName].append(nodeName)

            # add the edge to the previous node
            if prevNode is not None:
                self.add_edge(prevNode, nodeName)
            prevNode = nodeName

    def addFlow(self, src: pgv.Node, dst: pgv.Node):
        srcName = src.name
        dstName = dst.name
        self.add_edge(self.bbToNodes[srcName][-1], self.bbToNodes[dstName][0])


def cfg2fsm(cfgraph: CFGraph) -> FSM:
    fsm = FSM(strict=False, directed=True)

    # Add basic blocks to FSM
    for node in cfgraph.nodes():
        fsm.addBB(node)

    # Add flows between basic blocks in FSM
    for edge in cfgraph.edges():
        src = edge[0]
        dst = edge[1]
        fsm.addFlow(src, dst)

    return fsm
