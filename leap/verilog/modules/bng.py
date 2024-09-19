from .dfg import *
from .assignment import *
import pygraphviz as pgv

class BNGraph:
    def __init__(self):
        self.assignments = []
        self.var2assigns = {}
        
    def addAssignment(self, assignment: Assignment):
        self.assignments.append(assignment)
        
        variableName = assignment.target.name
        if variableName not in self.var2assigns:
            self.var2assigns[variableName] = []
        self.var2assigns[variableName].append(assignment)
    
    def traverse(self):
        # link the assignments by the names
        pass
    
    def exportDOT(self, filename: str, varName: str = None, params: dict = {}):
        G = pgv.AGraph(strict=False, directed=True)
        G.graph_attr['splines'] = 'ortho'
        G.graph_attr['rankdir'] = 'TB'     # Top-to-bottom layout

        # parse the params
        skipConstants = params.get('skipConstants', True)

        assignmentsToExport = self.assignments if varName is None else self.var2assigns[varName]
        
        for i, assignment in enumerate(assignmentsToExport):
            
            if skipConstants and assignment.expression.isConstant():
                continue
            
            id_lhs = self.exportDOTRec(G, assignment.target)
            id_rhs = self.exportDOTRec(G, assignment.expression)
            
            # add the edge from the rhs to the lhs
            G.add_edge(id_rhs, id_lhs, style='dashed', color='red', xlabel=f'val{i}')
            
            # add the edge from the condition to the lhs
            if assignment.condition is not None:
                id_con = self.exportDOTRec(G, assignment.condition)
                G.add_edge(id_con, id_lhs, style='dashed', color='blue', xlabel=f'cond{i}')
            
        G.layout(prog='dot')
        G.draw(filename)

    def exportDOTRec(self, G: pgv.AGraph, node: DFGNode):
        idx = G.number_of_nodes()
        idx = node.toString() if node.isVariable() else f"node{idx}"
        G.add_node(idx, label=node.name, shape='box' if isinstance(node, VariableNode) else 'ellipse')
        for child in node.children:
            child_idx = self.exportDOTRec(G, child)
            G.add_edge(child_idx, idx)
        return idx