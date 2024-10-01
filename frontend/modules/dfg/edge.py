from .node import *
from .port import *


@dataclass
class BNEdge:
    target: BNode


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
        eventStr = self.event.toString() if self.event is not None else ""
        condStr = self.condition.toString() if self.condition is not None else ""
        return f"always @({eventStr}) if ({condStr}) {self.target.toString()} = {self.expression.toString()}"


@dataclass
class BlockingAssignment(Assignment):
    isBlocking: bool = True


@dataclass
class NonBlockingAssignment(Assignment):
    isBlocking: bool = False
