#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 21:29:47
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:58:04
"""

from enum import Enum
from .dfg import *


class PortDirection(Enum):
    INPUT = "input"
    OUTPUT = "output"
    INOUT = "inout"

    @staticmethod
    def fromString(direction: str):
        if direction == "input":
            return PortDirection.INPUT
        elif direction == "output":
            return PortDirection.OUTPUT
        elif direction == "inout":
            return PortDirection.INOUT
        else:
            return None

    @staticmethod
    def toString(direction: "PortDirection"):
        return direction.value.lower() if direction is not None else None


class PortType(Enum):
    WIRE = "wire"
    REG = "reg"
    INTEGER = "integer"
    REAL = "real"
    TIME = "time"
    PARAMETER = "parameter"
    LOCALPARAM = "localparam"

    @staticmethod
    def fromString(type: str):
        if type == "wire":
            return PortType.WIRE
        elif type == "reg":
            return PortType.REG
        elif type == "integer":
            return PortType.INTEGER
        elif type == "real":
            return PortType.REAL
        elif type == "time":
            return PortType.TIME
        elif type == "parameter":
            return PortType.PARAMETER
        elif type == "localparam":
            return PortType.LOCALPARAM
        else:
            return None

    @staticmethod
    def toString(type: "PortType"):
        return type.value if type is not None else None


class Port:
    def __init__(
        self,
        variable: DFGNode,
    ):
        self.variable: DFGNode = variable
        self.range: Range = None
        self.direction: PortDirection = None
        self.type: PortType = None

    def setRange(self, range: Range):
        if self.range is None and range is not None:
            self.range = range
            return True
        return False

    def setHeader(self, header: tuple):
        direction, type = header
        return self.setDirection(direction) and self.setType(type)

    def setDirection(self, direction: PortDirection):
        if self.direction is None and direction is not None:
            assert isinstance(direction, PortDirection)
            self.direction = direction
            return True
        return False

    def setType(self, type: str):
        if type is not None:
            assert self.type is None, "Type already set"
            assert isinstance(type, PortType)
            self.type = type
            return True
        return False

    def setAll(self, direction: PortDirection, type: str, range: Range):
        self.setDirection(direction)
        self.setType(type)
        self.setRange(range)

    def getType(self) -> PortType:
        return self.type

    def getPortName(self) -> str:
        return self.variable.toString()

    def getRange(self) -> Range:
        return self.range

    def getHeader(self):
        return (self.direction, self.type)

    def __repr__(self):
        direction_str = (
            "(" + self.direction.value + ")" if self.direction is not None else ""
        )
        return f"Port({self.name}, {direction_str}, {self.type}, {self.range})"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Port):
            print(f"Type mismatch: {type(value)}")
            return False
        if self.variable != value.variable:
            print(f"Variable mismatch: {self.variable} != {value.variable}")
            return False
        if self.direction != value.direction:
            print(f"Direction mismatch: {self.direction} != {value.direction}")
            return False
        if self.getType() != value.getType():
            print(f"Type mismatch: {self.getType()} != {value.getType()}, signal = {self.variable}")
            return False
        if self.range != value.range:
            return False
        return True

    @property
    def name(self):
        return self.variable.name


def portToString(port: Port):
    portDirString = ""
    if port.direction is not None:
        portDirString = PortDirection.toString(port.direction) + " "
    typeString = (
        PortType.toString(port.type) + " " if port.type is not None else "wire "
    )

    # range is optional, the space is to be consistent with the space in the middle
    rangeString = f"{rangeToString(port.range)} " if port.range is not None else " "
    return f"{portDirString}{typeString}{rangeString}{port.name}"


class BasicPort(Port):
    def __init__(
        self,
        name: str,
        direction: PortDirection,
        type: str = "wire",
        range: tuple = None,
    ):
        super().__init__(name)
        self.setDirection(direction)
        self.setType(PortType.fromString(type))
        self.setRange(range)


class OutputPort(BasicPort):
    def __init__(
        self,
        name: str,
        type: str = "wire",
        range: tuple = None,
    ):
        super().__init__(name, PortDirection.OUTPUT, type, range)


class InputPort(BasicPort):
    def __init__(
        self,
        name: str,
        type: str = "wire",
        range: tuple = None,
    ):
        super().__init__(name, PortDirection.INPUT, type, range)


class Frame:
    def __init__(self) -> None:
        self.portDefs: dict = {}
        self.ioPorts: set = set()

    def addPort(self, port: Port) -> None:
        name = port.getPortName()
        if name in self.portDefs:
            self.getPort(name).setAll(port.direction, port.type, port.range)
        else:
            self.portDefs[name] = port

        if port.direction is not None:
            self.ioPorts.add(name)

    def addPorts(self, ports: list) -> None:
        for port in ports:
            self.addPort(port)

    def getIOs(self) -> set:
        return self.ioPorts

    def getPorts(self) -> dict:
        return self.portDefs

    def getPortNames(self) -> list:
        return list(self.portDefs.keys())

    def getPort(self, portName: str) -> Port:
        return self.portDefs[portName]

    def getVariableType(self, variableName: str):
        return self.portDefs[variableName].getType()

    def getPortsByDir(self, portDir: PortDirection) -> list:
        return [
            port.name for port in self.portDefs.values() if port.direction == portDir
        ]
    
    def getPortsByType(self, portType: PortType) -> list:
        return [
            port.name for port in self.portDefs.values() if port.type == portType
        ]

    @property
    def numInputs(self) -> int:
        return len(self.getPortsByDir(PortDirection.INPUT))

    @property
    def numOutputs(self) -> int:
        return len(self.getPortsByDir(PortDirection.OUTPUT))

    @property
    def numInouts(self) -> int:
        return len(self.getPortsByDir(PortDirection.INOUT))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Frame):
            return False
        # compare ports
        for port in self.getPortNames():
            if port not in other.getPortNames():
                print(f"Port {port} not found in other")
                return False
            if self.getPort(port) != other.getPort(port):
                print(f"Port {port} in self is not equal to port {port} in other")
                return False
        return True
