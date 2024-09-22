from .node import *

highlightColors_extended = {
    "CYAN": {"fillcolor": "#B3E5FC", "fontcolor": "#0288D1"},  # Light cyan, Dark cyan
    "INDIGO": {
        "fillcolor": "#C5CAE9",
        "fontcolor": "#303F9F",
    },  # Light indigo, Dark indigo
    "VIOLET": {
        "fillcolor": "#D1C4E9",
        "fontcolor": "#512DA8",
    },  # Light violet, Dark violet
    "TEAL": {"fillcolor": "#B2DFDB", "fontcolor": "#00796B"},  # Light teal, Dark teal
    "GREY_BLUE": {
        "fillcolor": "#B0BEC5",
        "fontcolor": "#37474F",
    },  # Light grey-blue, Dark grey-blue
    "GREEN": {
        "fillcolor": "#C8E6C9",
        "fontcolor": "#388E3C",
    },  # Light green, Dark green
    "PURPLE": {
        "fillcolor": "#E1BEE7",
        "fontcolor": "#7B1FA2",
    },  # Light purple, Dark purple
    "ORANGE": {
        "fillcolor": "#FFE0B2",
        "fontcolor": "#FF6F00",
    },  # Light orange, Dark orange
}


class BNGraph:
    def __init__(self):
        self.assignments = []
        self.var2assigns = {}
        self.graph = None

    def addAssignment(self, assignment):
        self.assignments.append(assignment)
        assert isinstance(assignment.target, DFGNode), f"Expected DFGNode, got {assignment.target}, {type(assignment.target)}"
        variableName = assignment.target.name
        if variableName not in self.var2assigns:
            self.var2assigns[variableName] = []
        self.var2assigns[variableName].append(len(self.assignments) - 1)

    def removeAssignment(self, idx: int):
        self.assignments[idx] = None

    def removeVariable(self, variableName: str):
        for idx in self.var2assigns[variableName]:
            self.removeAssignment(idx)
        del self.var2assigns[variableName]

    def updateAssignments(self):
        self.assignments = [
            assignment for assignment in self.assignments if assignment is not None
        ]
        self.var2assigns = {}
        for idx, assignment in enumerate(self.assignments):
            variableName = assignment.target.name
            if variableName not in self.var2assigns:
                self.var2assigns[variableName] = []
            self.var2assigns[variableName].append(idx)

    def isDefined(self, variableName: str):
        return variableName in self.var2assigns

    def getAssignmentsOf(self, variableName: str):
        if variableName not in self.var2assigns:
            return []
        for idx in self.var2assigns[variableName]:
            yield self.assignments[idx]

    def getAssignNode(self, variableName: str):
        # get the node corresponding to the variable
        for assignment in self.getAssignmentsOf(variableName):
            # should be only one
            return assignment.expression
        return None

    def getDependencies(self, variableName: str, excludeControls=False):
        # get the dependencies of the variable
        dependencies = []
        for assignment in self.getAssignmentsOf(variableName):
            root = assignment.expression
            cond = assignment.condition
            dependencies.extend(self.getDependenciesRec(root))
            if not excludeControls and cond is not None:
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

    def expandAssignment(self):
        # extract the assignment of the variable, merge the predecessors
        # until we reach the inputs
        for assignment in self.assignments:
            root = assignment.expression
            newNode = self._expandAssignmentRec(root)
            assignment.expression = newNode

    def _expandAssignmentRec(self, node: DFGNode) -> DFGNode:
        # expand the assignment recursively
        if node.isVariable():
            depNode = self.getAssignNode(node.name)
            if depNode is not None:
                return self._expandAssignmentRec(depNode)
            return node.copy()

        newNode: DFGNode = node.copy()
        children = []
        for child in node.children:
            childNode = self._expandAssignmentRec(child)
            children.append(childNode)
        newNode.children = children
        return newNode
