#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 21:29:47
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:58:04
"""

from enum import Enum, auto
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
        name: str,
    ):
        self.name = name
        self.range = None
        self.direction = None
        self.type = None

    def setRange(self, range: tuple):
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
        if self.type is None and type is not None:
            assert isinstance(type, PortType)
            self.type = type
            return True
        return False

    def setAll(self, direction: PortDirection, type: str, range: tuple):
        return (
            self.setDirection(direction) and self.setType(type) and self.setRange(range)
        )

    def getType(self):
        return self.type

    def getPortName(self):
        return self.name

    def getRange(self):
        return self.range

    def getHeader(self):
        return (self.direction, self.type)

    def __repr__(self):
        direction_str = (
            "(" + self.direction.value + ")" if self.direction is not None else ""
        )
        return f"Port({self.name} {direction_str})"


def portToString(port: Port):
    portDirString = ""
    if port.direction is not None:
        portDirString = PortDirection.toString(port.direction) + " "
    typeString = port.type + " " if port.type is not None else ""

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
        self.setType(type)
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
        self.portDefs = {}
        self.ioPorts = set()

    def addPort(self, port: Port):
        name = port.getPortName()
        if name in self.portDefs:
            self.portDefs[name].setRange(port.getRange())
            self.portDefs[name].setHeader(port.getHeader())
        else:
            self.portDefs[name] = port

        if port.direction is not None:
            self.ioPorts.add(name)

    def addPorts(self, ports: list):
        for port in ports:
            self.addPort(port)

    def getIOs(self) -> set:
        return self.ioPorts

    def getPorts(self) -> dict:
        return self.portDefs

    def getPortNames(self) -> list:
        return list(self.portDefs.keys())

    def getPort(self, portName: str):
        return self.portDefs[portName]

    def getVariableType(self, variableName: str):
        return self.portDefs[variableName].getType()

    def getPortsByType(self, portType: PortDirection):
        return [
            port.name for port in self.portDefs.values() if port.direction == portType
        ]

    @property
    def numInputs(self) -> int:
        return len(self.getPortsByType(PortDirection.INPUT))

    @property
    def numOutputs(self) -> int:
        return len(self.getPortsByType(PortDirection.OUTPUT))

    @property
    def numInouts(self) -> int:
        return len(self.getPortsByType(PortDirection.INOUT))
