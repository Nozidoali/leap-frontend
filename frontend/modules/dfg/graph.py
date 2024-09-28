from dataclasses import dataclass, field
from typing import Optional, Dict, List

from .node import *


@dataclass
class Assignment:
    """
    Assignments are the elementary statements in the module.

    - **target** (DFGNode): the target variable
    - **expression** (DFGNode): the expression to be assigned to the target
    - **condition** (DFGNode): the condition under which the assignment is valid
    - **event** (DFGNode): the event under which the assignment is valid
    """

    target: DFGNode
    expression: DFGNode
    condition: Optional[DFGNode] = None
    event: Optional[DFGNode] = None
    isBlocking: bool = True

    def addCondition(self, condition: DFGNode):
        if condition is None:
            return
        if self.condition is None:
            self.condition = condition
        else:
            self.condition = OPNode("&&", OPType.BINARY_AND, self.condition, condition)
        return self

    def setEvent(self, event: DFGNode):
        self.event = event
        return self

    def __repr__(self) -> str:
        if self.isBlocking:
            return f"{self.target} = {self.expression}"
        return f"{self.target} <= {self.expression} ({self.condition})"

    def replaceVariable(self, old: str, new: str):
        self.target.replaceVariable(old, new)
        self.expression.replaceVariable(old, new)
        if self.condition is not None:
            self.condition.replaceVariable(old, new)


@dataclass
class BlockingAssignment(Assignment):
    def __post_init__(self):
        self.isBlocking = True


@dataclass
class NonBlockingAssignment(Assignment):
    def __post_init__(self):
        self.isBlocking = False


class BNGraph:
    def __init__(self):
        self.assignments: List[Assignment] = []
        self.var2assigns: Dict[str, List[int]] = {}

    def addAssignment(self, assignment: Assignment) -> None:
        self.assignments.append(assignment)
        assert isinstance(
            assignment.target, DFGNode
        ), f"Expected DFGNode, got {assignment.target}, {type(assignment.target)}"
        variableName = assignment.target.name
        if variableName not in self.var2assigns:
            self.var2assigns[variableName] = []
        self.var2assigns[variableName].append(len(self.assignments) - 1)

    def removeAssignment(self, idx: int) -> None:
        self.assignments[idx] = None

    def removeVariable(self, variableName: str):
        for idx in self.var2assigns[variableName]:
            self.removeAssignment(idx)
        del self.var2assigns[variableName]

    def updateAssignments(self) -> None:
        self.assignments = [
            assignment for assignment in self.assignments if assignment is not None
        ]
        self.var2assigns = {}
        for idx, assignment in enumerate(self.assignments):
            variableName = assignment.target.name
            if variableName not in self.var2assigns:
                self.var2assigns[variableName] = []
            self.var2assigns[variableName].append(idx)

    def isDefined(self, variableName: str) -> bool:
        return variableName in self.var2assigns

    def getAssignmentsOf(self, variableName: str) -> List[Assignment]:
        if variableName not in self.var2assigns:
            return []
        return [self.assignments[idx] for idx in self.var2assigns[variableName]]

    def getAssignNode(self, variableName: str) -> Optional[DFGNode]:
        # get the node corresponding to the variable
        for assignment in self.getAssignmentsOf(variableName):
            # should be only one
            return assignment.expression
        return None

    def getDependencies(self, variableName: str, excludeControls=False) -> List[str]:
        # get the dependencies of the variable
        dependencies = []
        for assignment in self.getAssignmentsOf(variableName):
            root = assignment.expression
            cond = assignment.condition
            dependencies.extend(self.getDependenciesRec(root))
            if not excludeControls and cond is not None:
                dependencies.extend(self.getDependenciesRec(cond))
        return dependencies

    def getDependenciesRec(self, node: DFGNode) -> List[str]:
        # get the dependencies of the node
        if node.isVariable():
            return [node.name]
        dependencies = []
        for child in node.children:
            dependencies.extend(self.getDependenciesRec(child))
        return dependencies

    def expandAssignment(self) -> None:
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

    def traverseAndApply(self, func: callable, postOrder: bool = True) -> None:
        visited = set()
        for assignment in self.assignments:
            root = assignment.expression
            self._traverseAndApplyRec(root, func, visited, postOrder)

    def _traverseAndApplyRec(
        self, node: DFGNode, func: callable, visited: set, postOrder: bool
    ) -> None:
        # traverse the graph and apply the function

        # apply the function, this is a pre-order traversal
        if not postOrder:
            func(node)

        if node.isVariable():
            if node.toString() in visited:
                return
            visited.add(node.toString())
            depNode = self.getAssignNode(node.name)
            if depNode is not None:
                self._traverseAndApplyRec(depNode, func, visited, postOrder)

        # traverse the children
        for child in node.children:
            self._traverseAndApplyRec(child, func, visited, postOrder)

        # apply the function, this is a post-order traversal
        if postOrder:
            func(node)

    def getVariableNames(self) -> List[str]:
        return list(self.var2assigns.keys())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BNGraph):
            return False
        # compare assignments
        for var in self.getVariableNames():
            if var not in other.getVariableNames():
                print(f"Variable {var} not found in other")
                return False
            assignments1 = self.getAssignmentsOf(var)
            assignments2 = other.getAssignmentsOf(var)
            assert len(assignments1) == len(
                assignments2
            ), f"Assignment lengths are not equal: {len(assignments1)} != {len(assignments2)}"
            for i in range(len(assignments1)):
                if assignments1[i] != assignments2[i]:
                    print(
                        f"Assignment {i} is not equal, {assignments1[i]} != {assignments2[i]}"
                    )
                    return False
        return True

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
