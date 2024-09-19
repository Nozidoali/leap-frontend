from .dfg import *
from .assignment import *
import pygraphviz as pgv

class BNGraph:
    def __init__(self):
        self.assignments = []
        self.var2assigns = {}
        self.graph = None
        
    def addAssignment(self, assignment: Assignment):
        self.assignments.append(assignment)
        
        variableName = assignment.target.name
        if variableName not in self.var2assigns:
            self.var2assigns[variableName] = []
        self.var2assigns[variableName].append(assignment)
    
    def traverse(self):
        # link the assignments by the names
        pass
    
    def writeDOT(self, filename: str):
        self.graph.write(filename)
    
    def exportDOT(self, varName: str = None, params: dict = {}):
        self.graph = pgv.AGraph(strict=False, directed=True)
        self.graph.graph_attr['splines'] = 'ortho'
        self.graph.graph_attr['rankdir'] = 'TB'     # Top-to-bottom layout

        # parse the params
        skipConstants = params.get('skipConstants', True)
        extractFSM = params.get('extractFSM', True)

        assignmentsToExport = self.assignments if varName is None else self.var2assigns[varName]
        
        for i, assignment in enumerate(assignmentsToExport):
            
            if skipConstants and assignment.expression.isConstant():
                continue
            
            id_lhs = self.exportDOTRec(assignment.target)
            id_rhs = self.exportDOTRec(assignment.expression)
            
            # add the edge from the rhs to the lhs
            self.graph.add_edge(id_rhs, id_lhs, style='dashed', color='red', xlabel=f'val{i}')
            
            # add the edge from the condition to the lhs
            if assignment.condition is not None:
                id_con = self.exportDOTRec(assignment.condition)
                self.graph.add_edge(id_con, id_lhs, style='dashed', color='blue', xlabel=f'cond{i}')
        
        if extractFSM:
            # extract the FSM into a subgraph
            fsmGraph = self.graph.add_subgraph(name='cluster_fsm', label='FSM', style='dashed', color='blue')
            fsmGraph.graph_attr['rankdir'] = 'LR'     # Left-to-right layout
            
            # add the nodes
            fsmPorts = ["next_state", "finish"]
            self.applyToFrame(fsmPorts, lambda node: self._moveToSubgraph(node, self.graph, fsmGraph))
            self.applyToFrame(fsmPorts, self._highlightNode)

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
        # graph.delete_node(node)
        subgraph.add_node(node, **node.attr)
    
    @staticmethod
    def _highlightNode(node: pgv.Node):
        node.attr['color'] = "#0288D1"
        node.attr['style'] = "filled"
        node.attr['fillcolor'] = "#B3E5FC"
        # text color
        node.attr['fontcolor'] = "#0288D1"
    
    def colorFrame(self, variables: list):
        self.applyToFrame(variables, self._highlightNode)
    
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