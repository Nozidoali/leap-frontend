from typing import List, Optional, Tuple
from dataclasses import dataclass
from abc import ABC, abstractmethod

from .node import *
from .port import *


@dataclass
class BNEdge:
    target: BNode

    @abstractmethod
    def toString(self) -> str:
        pass


@dataclass
class Assignment(BNEdge):
    """
    Assignments are the elementary statements in the module.

    - **target** (BNode): the target variable
    - **expression** (BNode): the expression to be assigned to the target
    - **condition** (BNode): the condition under which the assignment is valid
    - **event** (BNode): the event under which the assignment is valid
    """

    # TODO: decide if we need to change target directly to a Port
    expression: BNode
    condition: Optional[BNode] = None
    event: Optional[BNode] = None
    isBlocking: bool = True
    targetType: PortType = PortType.WIRE
    isProcedural: bool = False

    def addCondition(self, condition: BNode):
        if condition is None:
            return
        self.condition = (
            condition
            if self.condition is None
            else OPNode("&&", OPType.BINARY_AND, self.condition, condition)
        )
        return self

    def setEvent(self, event: BNode):
        assert isinstance(event, BNode)
        self.event = event
        return self

    def replaceVariable(self, old: str, new: str):
        self.target.replaceVariable(old, new)
        self.expression.replaceVariable(old, new)
        if self.condition is not None:
            self.condition.replaceVariable(old, new)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Assignment):
            print(f"Expected Assignment, got {type(other)}")
            return False
        if self.target != other.target:
            print(f"Target mismatch: {self.target} != {other.target}")
            return False
        if self.expression != other.expression:
            print(f"Expression mismatch: {self.expression} != {other.expression}")
            return False
        if self.condition != other.condition:
            print(f"Condition mismatch: {self.condition} != {other.condition}")
            return False
        if self.event != other.event:
            print(f"Event mismatch: {self.event} != {other.event}")
            return False
        return True

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

    def toString(self) -> str:
        # NOTE: this should not be used for verilog generation
        # Only for debugging purposes
        # Use `assignmentToString` instead
        retString = ""

        target = self.target.toString()
        expression = self.expression.toString()
        assignOp = "=" if self.isBlocking else "<="
        condition = self.condition
        assignHead = (
            "assign "
            if self.targetType == PortType.WIRE and not self.isProcedural
            else ""
        )

        if self.event is not None:
            retString += f"{self.event.toString()} begin\n"

        assignBody = f"{assignHead}{target} {assignOp} {expression};"
        # TODO: consider wire/latch/reg
        if condition is not None:
            condition = condition.toString()
            retString += f"if ({condition}) begin\n\t{assignBody}\nend\n"
        else:
            retString += f"{assignBody}\n"

        if self.event is not None:
            retString += "end\n"

        return retString


@dataclass
class BlockingAssignment(Assignment):
    isBlocking: bool = True


@dataclass
class NonBlockingAssignment(Assignment):
    isBlocking: bool = False


@dataclass
class RegAssignment(Assignment):
    targetType: PortType = PortType.REG
    isBlocking: bool = False


@dataclass
class WireAssignment(Assignment):
    targetType: PortType = PortType.WIRE
    isBlocking: bool = True


@dataclass
class LatchAssignment(Assignment):
    targetType: PortType = PortType.REG
    isBlocking: bool = True


@dataclass
class CaseAssignment(BNEdge):
    caseVariable: BNode
    cases: List[Tuple[BNode, BNEdge]] = field(default_factory=list)
    isBlocking: bool = True
    targetType: PortType = PortType.WIRE
    event: BNode = None

    def addCase(self, caseValue: BNode, expression: BNEdge):
        # assert isinstance(caseValue, BNode), f"Expected BNode, got {type(caseValue)}"
        assert isinstance(
            expression, BNEdge
        ), f"Expected BNEdge, got {type(expression)}"
        self.cases.append((caseValue, expression))
        return self

    def addDefaultCase(self, expression: BNEdge):
        self.addCase(None, expression)
        return self

    def toString(self) -> str:
        caseStr = ""
        if self.event is not None:
            caseStr += f"{self.event.toString()} begin\n"
        caseStr += f"case ({self.caseVariable.toString()})"
        for caseValue, expression in self.cases:
            if caseValue is None:
                caseStr += f"\ndefault:\n{expression.toString()}"
                continue
            caseStr += f"\n{caseValue.toString()}:\n{expression.toString()}"
        caseStr += "\nendcase\n"
        if self.event is not None:
            caseStr += "end\n"
        return caseStr


@dataclass
class ConditionalAssignment(BNEdge):
    """
    These conditions are order sensitive.
    The first is the highest priority (i.e. the first condition that is true is executed)
    The last could be a default condition (None)
    """

    conditions: List[Tuple[BNode, Assignment]] = field(default_factory=list)
    isBlocking: bool = True
    targetType: PortType = PortType.WIRE
    event: BNode = None

    def addBranch(
        self, condition: BNode, expression: Assignment
    ) -> "ConditionalAssignment":
        assert isinstance(
            expression, Assignment
        ), f"Expected Assignment, got {type(expression)}"
        self.conditions.append((condition, expression))
        return self

    def addDefaultBranch(self, expression: Assignment) -> "ConditionalAssignment":
        self.addBranch(None, expression)
        return self

    def toString(self) -> str:
        retString = ""
        if self.event is not None:
            retString += f"{self.event.toString()} begin\n"
        for i, (condition, expression) in enumerate(self.conditions):
            if i != 0:
                retString += "else "
            if condition is None:
                retString += f"{expression.toString()}"
                continue
            retString += f"if ({condition.toString()}) {expression.toString()}"
        if self.event is not None:
            retString += "end\n"
        return retString
