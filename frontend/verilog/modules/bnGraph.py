from .dfg import *
from .assignment import *

highlightColors_extended = {
    'CYAN': {"fillcolor": "#B3E5FC", "fontcolor": "#0288D1"},  # Light cyan, Dark cyan
    'INDIGO': {"fillcolor": "#C5CAE9", "fontcolor": "#303F9F"},  # Light indigo, Dark indigo
    'VIOLET': {"fillcolor": "#D1C4E9", "fontcolor": "#512DA8"},  # Light violet, Dark violet
    'TEAL': {"fillcolor": "#B2DFDB", "fontcolor": "#00796B"},  # Light teal, Dark teal
    'GREY_BLUE': {"fillcolor": "#B0BEC5", "fontcolor": "#37474F"},  # Light grey-blue, Dark grey-blue
    'GREEN': {"fillcolor": "#C8E6C9", "fontcolor": "#388E3C"},  # Light green, Dark green
    'PURPLE': {"fillcolor": "#E1BEE7", "fontcolor": "#7B1FA2"},  # Light purple, Dark purple
    'ORANGE': {"fillcolor": "#FFE0B2", "fontcolor": "#FF6F00"},  # Light orange, Dark orange
}

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
        self.var2assigns[variableName].append(len(self.assignments) - 1)
    
    def isDefined(self, variableName: str):
        return variableName in self.var2assigns
    
    def getAssignmentsOf(self, variableName: str):
        for idx in self.var2assigns[variableName]:
            yield self.assignments[idx]
    
    def getDependencies(self, variableName: str):
        # get the dependencies of the variable
        dependencies = []
        for assignment in self.getAssignmentsOf(variableName):
            root = assignment.expression
            cond = assignment.condition
            dependencies.extend(self.getDependenciesRec(root))
            if cond is not None:
                dependencies.extend(self.getDependenciesRec(cond))
        return dependencies
            
    def getDependenciesRec(self, node: DFGNode):
        # get the dependencies of the node
        if node.isVariable():
            return [node.name]
        dependencies = []
        for child in node.children:
            dependencies.extend(self.getDependenciesRec(child))
        return dependencies
    
