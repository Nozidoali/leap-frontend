from .dotGraph import *
import re


class ExtendedGraph(DotGraph):
    def __init__(self):
        super().__init__()

    def exportDOT(self, varName: str = None, params: dict = {}):
        super().exportDOT(varName, params)

        extractFSM = params.get("extractFSM", True)
        extractCIP = params.get("extractCIP", True)
        extractARG = params.get("extractARG", True)
        extractREG = params.get("extractREG", True)

        if extractFSM:
            # extract the FSM into a subgraph
            fsmGraph = self.graph.add_subgraph(
                name="cluster_fsm", label="FSM", style="dashed", color="blue"
            )
            fsmGraph.graph_attr["rankdir"] = "LR"  # Left-to-right layout

            # add the nodes
            fsmPorts = ["next_state", "finish"]
            self.applyToFrame(
                fsmPorts, lambda node: self._moveToSubgraph(node, self.graph, fsmGraph)
            )
            self.applyToFrame(fsmPorts, lambda node: self._highlightNode(node, "CYAN"))

        if extractCIP:
            # memory address and memory out
            CIPpairs = []
            for node in self.graph.nodes():
                # e.g. main_0_b_address_a and main_0_b_out_a
                if re.match(r".*address.*", node.attr["label"]):
                    try:
                        outNode = self.graph.get_node(
                            node.attr["label"].replace("address", "out")
                        )
                    except KeyError:
                        outNode = None
                    try:
                        inNode = self.graph.get_node(
                            node.attr["label"].replace("address", "in")
                        )
                    except KeyError:
                        inNode = None
                    CIPpairs.append((node, outNode, inNode))

            for i, (addressNode, outNode, inNode) in enumerate(CIPpairs):
                cipGraph = self.graph.add_subgraph(
                    name=f"cluster_cip{i}", label="CIP", style="dashed", color="green"
                )
                cipGraph.graph_attr["rankdir"] = "TB"

                for node in [addressNode, outNode, inNode]:
                    if node is not None:
                        self._moveToSubgraph(node, self.graph, cipGraph)
                        self._highlightNode(node, "GREEN")

        if extractARG:
            argGraph = self.graph.add_subgraph(
                name="cluster_arg", label="args", style="dashed", color="purple"
            )
            node: pgv.Node
            for node in self.graph.nodes():
                if node.attr["label"].startswith("arg"):
                    argGraph.graph_attr["rankdir"] = "LR"
                    self._moveToSubgraph(node, self.graph, argGraph)
                    self._highlightNode(node, "PURPLE")

        if extractREG:
            stages = {}
            for node in self.graph.nodes():
                # match the state number, the name should be ..._reg_stage<num>
                try:
                    stage = int(
                        re.search(r"_reg_stage(\d+)", node.attr["label"]).group(1)
                    )
                    if stage not in stages:
                        stages[stage] = []
                    stages[stage].append(node)
                except AttributeError:
                    continue

            for stage, nodes in stages.items():
                regGraph = self.graph.add_subgraph(
                    name=f"cluster_reg{stage}",
                    label=f"pipeline stage \#{stage}",
                    style="dashed",
                    color="orange",
                )
                regGraph.graph_attr["rankdir"] = "TB"
                for node in nodes:
                    self._moveToSubgraph(node, self.graph, regGraph)
                    self._highlightNode(node, "ORANGE")

        self.graph.layout(prog="dot")
