from dataclasses import dataclass, field
from typing import Optional, Dict, List

from .port import *
from .node import *
from .edge import *


class BNGraph:
    def __init__(self):
        self._assignments: List[BNEdge] = []
        self._var2assigns: Dict[str, List[int]] = {}

    def addAssignment(self, assignment: BNEdge) -> None:
        self._assignments.append(assignment)
        variableName = assignment.target.name
        if variableName not in self._var2assigns:
            self._var2assigns[variableName] = []
        self._var2assigns[variableName].append(len(self._assignments) - 1)

    def removeAssignment(self, idx: int) -> None:
        self._assignments[idx] = None

    def removeVariable(self, variableName: str):
        for idx in self._var2assigns[variableName]:
            self.removeAssignment(idx)
        del self._var2assigns[variableName]

    def updateAssignments(self) -> None:
        self._assignments = [
            assignment for assignment in self._assignments if assignment is not None
        ]
        self._var2assigns = {}
        for idx, assignment in enumerate(self._assignments):
            variableName = assignment.target.name
            if variableName not in self._var2assigns:
                self._var2assigns[variableName] = []
            self._var2assigns[variableName].append(idx)

    def substituteAssignments(
        self, old: List[int], new: List[BNEdge], lazyUpdate: bool = True
    ) -> None:
        for idx in old:
            self._assignments[idx] = None
        for assignment in new:
            self.addAssignment(assignment)
        if not lazyUpdate:
            self._reindex()

    def _reindex(self) -> None:
        self._var2assigns = {}
        newAssignments = []
        for idx, assignment in enumerate(self._assignments):
            if assignment is None:
                continue
            variableName = assignment.target.name
            if variableName not in self._var2assigns:
                self._var2assigns[variableName] = []
            self._var2assigns[variableName].append(len(newAssignments))
            newAssignments.append(assignment)
        self._assignments = newAssignments

    def getVariables(self) -> List[str]:
        return list(self._var2assigns.keys())

    def isDefined(self, variableName: str) -> bool:
        return variableName in self._var2assigns

    def getAssignments(self) -> List[BNEdge]:
        return [
            assignment for assignment in self._assignments if assignment is not None
        ]

    def getAssignmentsOf(self, variableName: str) -> List[Assignment]:
        if variableName not in self._var2assigns:
            return []
        return [self._assignments[idx] for idx in self._var2assigns[variableName]]

    def getAssignNode(self, variableName: str) -> Optional[BNode]:
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

    def getDependenciesRec(self, node: BNode) -> List[str]:
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
        for assignment in self._assignments:
            root = assignment.expression
            newNode = self._expandAssignmentRec(root)
            assignment.expression = newNode

    def _expandAssignmentRec(self, node: BNode) -> BNode:
        # expand the assignment recursively
        if node.isVariable():
            depNode = self.getAssignNode(node.name)
            if depNode is not None:
                return self._expandAssignmentRec(depNode)
            return node.copy()

        newNode: BNode = node.copy()
        children = []
        for child in node.children:
            childNode = self._expandAssignmentRec(child)
            children.append(childNode)
        newNode.children = children
        return newNode

    def traverseAndApply(self, func: callable, postOrder: bool = True) -> None:
        visited = set()
        for assignment in self._assignments:
            root = assignment.expression
            self._traverseAndApplyRec(root, func, visited, postOrder)

    def _traverseAndApplyRec(
        self, node: BNode, func: callable, visited: set, postOrder: bool
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
        return list(self._var2assigns.keys())

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BNGraph):
            return False
        # compare _assignments
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
                        f"Assignment {i} is not equal, \n{assignments1[i].toString()} \n!=\n {assignments2[i].toString()}"
                    )
                    return False
        return True

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)
