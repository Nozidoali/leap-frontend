#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 21:29:47
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:58:04
"""

from enum import Enum

from dataclasses import dataclass
from typing import Optional, Dict, Set
from .dfg import *


@dataclass
class Port:
    """
    A port is the elementary unit of a frame.
    """

    variable: BNode
    range: Optional[Range] = None
    direction: Optional[PortDirection] = None
    type: Optional[PortType] = None

    def setRange(self, range: Range):
        if range is not None:
            assert isinstance(range, Range)
            if self.range is not None and self.range != range:
                raise ValueError(
                    f"Range mismatch: {self.range} != {range}, signal = {self.variable}"
                )
            self.range = range
            return True
        return False

    def setHeader(self, header: tuple):
        direction, type = header
        return self.setDirection(direction) and self.setType(type)

    def setDirection(self, direction: PortDirection, override: bool = False) -> bool:
        if override:
            self.direction = direction
            return True
        if direction is not None:
            assert isinstance(direction, PortDirection)
            if self.direction is not None and self.direction != direction:
                raise ValueError(
                    f"Direction mismatch: {self.direction} != {direction}, signal = {self.variable}"
                )
            self.direction = direction
            return True
        return False

    def getDirection(self) -> PortDirection:
        return self.direction

    def setType(self, type: PortType, override: bool = False) -> bool:
        # NOTE: use type instead of getType() in this function
        # Otherwise, the type cannot be overwritten
        if override:
            self.type = type
            return True
        if type is not None:
            assert isinstance(type, PortType)
            if self.type is not None and self.type != type:
                raise ValueError(
                    f"Type mismatch: {self.type} != {type}, signal = {self.variable}"
                )
            self.type = type
            return True
        return False

    def setAll(self, direction: PortDirection, type: PortType, range: Range):
        self.setDirection(direction)
        self.setType(type)
        self.setRange(range)

    def getType(self) -> PortType:
        return self.type if self.type is not None else PortType.WIRE

    def getPortName(self) -> str:
        return self.variable.toString()

    def getRange(self) -> Range:
        return self.range

    def getHeader(self):
        return (self.direction, self.type)

    @property
    def isTrivial(self) -> bool:
        return self.direction is None and self.type is None and self.range is None

    # We need to override the __eq__ function to compare two ports
    # Because we need to make sure type WIRE is equal to None
    def __eq__(self, value: object) -> bool:
        if value is None:
            return False
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
            print(
                f"Type mismatch: {self.getType()} != {value.getType()}, signal = {self.variable}"
            )
            return False
        if self.range != value.range:
            return False
        return True

    @property
    def name(self):
        return self.variable.name

    @property
    def isPi(self):
        return self.direction == PortDirection.INPUT

    @property
    def isPo(self):
        return self.direction == PortDirection.OUTPUT


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


@dataclass
class OutputPort(Port):
    direction: PortDirection = PortDirection.OUTPUT


@dataclass
class InputPort(Port):
    direction: PortDirection = PortDirection.INPUT


@dataclass
class InoutPort(Port):
    direction: PortDirection = PortDirection.INOUT


@dataclass
class ParameterPort(Port):
    type: PortType = PortType.PARAMETER


@dataclass
class WirePort(Port):
    type: PortType = PortType.WIRE


@dataclass
class RegPort(Port):
    type: PortType = PortType.REG


class Frame:
    def __init__(self) -> None:
        self.portDefs: Dict[str, Port] = {}
        self.ioPorts: Set[str] = set()

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
        return [port.name for port in self.portDefs.values() if port.type == portType]

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

    def getFrame(self):
        return self

    def copy(self):
        frame = Frame()
        frame.addPorts(self.portDefs.values())
        return frame
