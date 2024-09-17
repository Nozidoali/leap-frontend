from .dfg import *
from .assignment import *
import pygraphviz as pgv

class BNGraph:
    def __init__(self):
        self.assignments = []
        
    def addAssignment(self, assignment: Assignment):
        self.assignments.append(assignment)
        
    def exportDOT(self, filename: str):
        G = pgv.AGraph(strict=False, directed=True)
        for assignment in self.assignments:
            id_rhs = self.exportGraphRec(G, assignment.expression)
            
            # add the edge from the rhs to the lhs
            id_lhs = self.exportGraphRec(G, assignment.target)
            G.add_edge(id_rhs, id_lhs)
            
            # add the edge from the condition to the lhs
            if assignment.condition is not None:
                id_con = self.exportGraphRec(G, assignment.condition)
                G.add_edge(id_con, id_lhs)
        G.layout(prog='dot')
        G.draw(filename)

    def exportGraphRec(self, G: pgv.AGraph, node):
        idx = G.number_of_nodes()
        G.add_node(idx, label=node.toString())
        for child in node.children:
            child_idx = self.exportGraphRec(G, child)
            G.add_edge(child_idx, idx)
        return idx