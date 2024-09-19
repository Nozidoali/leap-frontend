from .bnGraph import *
import pygraphviz as pgv

class DotGraph(BNGraph):
    def __init__(self):
        super().__init__()
        
    def writeDOT(self, filename: str):
        self.graph.write(filename)
    
    def exportDOT(self, varName: str = None, params: dict = {}):
        self.graph = pgv.AGraph(strict=False, directed=True)
        self.graph.graph_attr['splines'] = 'ortho'
        self.graph.graph_attr['rankdir'] = 'TB'     # Top-to-bottom layout

        # parse the params
        skipConstants = params.get('skipConstants', True)
        assignmentsToExport = self.assignments if varName is None else self.var2assigns[varName]
        
        for i, assignment in enumerate(assignmentsToExport):
            if skipConstants and assignment.expression.isConstant():
                continue
            
            id_lhs = self.exportDOTRec(assignment.target)
            id_rhs = self.exportDOTRec(assignment.expression)
            
            # add the edge from the rhs to the lhs
            self.graph.add_edge(id_rhs, id_lhs, xlabel=f'val{i}')
            
            # add the edge from the condition to the lhs
            if assignment.condition is not None:
                id_con = self.exportDOTRec(assignment.condition)
                self.graph.add_edge(id_con, id_lhs, style='dashed', color='red', xlabel=f'cond{i}')
        
        self.graph.layout(prog='dot')

    def exportDOTRec(self, node: DFGNode):
        idx = self.graph.number_of_nodes()
        idx = node.toString() if node.isVariable() else f"node{idx}"
        self.graph.add_node(idx, label=node.name, shape='box' if isinstance(node, VariableNode) else 'ellipse')
        for child in node.children:
            child_idx = self.exportDOTRec(child)
            self.graph.add_edge(child_idx, idx)
        return idx
    
    @staticmethod
    def _moveToSubgraph(node: pgv.Node, graph: pgv.AGraph, subgraph: pgv.AGraph):
        subgraph.add_node(node.name, **node.attr)
    
    @staticmethod
    def _highlightNode(node: pgv.Node, color: str = 'CYAN'):
        node.attr['color'] = highlightColors_extended[color]['fontcolor']
        node.attr['style'] = "filled"
        node.attr['fillcolor'] = highlightColors_extended[color]['fillcolor']
        # text color
        node.attr['fontcolor'] = highlightColors_extended[color]['fontcolor']
    
    def colorFrame(self, variables: list, color: str = 'CYAN'):
        self.applyToFrame(variables, self._highlightNode, color)
    
    def applyToFrame(self, variables: list, func: callable):
        # color the nodes reachable from the current node
        assert self.graph is not None
        for node in self.graph.nodes():
            if node.attr['label'] in variables:
                self.applyToSuccessorsRec(node, set(), func)
                self.applyToPredecessorsRec(node, set(), func)

    def applyToSuccessorsRec(self, node: pgv.Node, visited: set, func: callable):
        func(node)
        visited.add(node)
        for child in self.graph.successors(node):
            if child not in visited:
                self.applyToSuccessorsRec(child, visited, func)
                
    def applyToPredecessorsRec(self, node: pgv.Node, visited: set, func: callable):
        func(node)
        visited.add(node)
        for child in self.graph.predecessors(node):
            if child not in visited:
                self.applyToPredecessorsRec(child, visited, func)