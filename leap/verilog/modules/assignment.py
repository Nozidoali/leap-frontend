#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-01 13:14:40
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-01 20:28:12
"""

from .expression import *

from enum import Enum


class AssignmentType(Enum):
    BLOCKING = "="
    NON_BLOCKING = "<="

    @staticmethod
    def fromString(s: str):
        if s == "=":
            return AssignmentType.BLOCKING
        if s == "<=":
            return AssignmentType.NON_BLOCKING
        raise ValueError(f"Unknown assignment type {s}")


class Assignment:
    def __init__(self, target, expression, condition=None) -> None:
        self.target = target
        self.expression = expression
        self.condition = condition
        self.type = None

    def setCondition(self, condition):
        self.condition = condition

    def setType(self, assignment_type: AssignmentType | str):
        if isinstance(assignment_type, str):
            if assignment_type == "blocking_assignment":
                self.type = AssignmentType.BLOCKING
            elif assignment_type == "non_blocking_assignment":
                self.type = AssignmentType.NON_BLOCKING
            else:
                raise ValueError(f"Unknown assignment type {assignment_type}")
        elif isinstance(assignment_type, AssignmentType):
            self.type = assignment_type
        else:
            raise ValueError(f"Unknown assignment type {assignment_type}")

    @property
    def isBlocking(self):
        return self.type == AssignmentType.BLOCKING

    def __repr__(self) -> str:
        return f"{self.target} = {self.expression} ({self.condition})"

    def addCondition(self, condition: DFGNode):
        if condition is None:
            return

        if self.condition is None:
            self.condition = condition
        else:
            self.condition = createBinaryOpNode(BOPType.AND, self.condition, condition)
