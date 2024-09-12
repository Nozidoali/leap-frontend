#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 22:33:09
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-23 23:19:24
"""

from ...verilog import *
from .headerWriter import *
from .dfgWriter import *


def writeModuleHeader(f, module: Module):
    name = module.getName()
    f.write(f"module {name}\n")
    f.write("(\n")
    ports = module.getPortList()
    portString = []
    for port in ports:
        portString.append(f"\t{port}")

    f.write(",\n".join(portString))
    f.write("\n")
    f.write(");\n\n")


def portToString(port: Port):
    portDirString = ""
    if port.direction is not None:
        portDirString = PortDirection.toString(port.direction) + " "
    typeString = port.type + " " if port.type is not None else ""

    # range is optional, the space is to be consistent with the space in the middle
    rangeString = f"{port.range} " if port.range is not None else " "
    return f"{portDirString}{typeString}{rangeString}{port.name}"


def writeParameters(f, module: Module):
    parameters: dict = module.getParameters()

    for key, value in parameters.items():
        parameter: Parameter = value
        rangeString = f"{parameter.range} " if parameter.range is not None else ""
        f.write(f"parameter {rangeString}{parameter.name} = {parameter.value};\n")

    f.write("\n")


def writeInternalSignals(f, module: Module):
    for signalName in module.getInternalSignalList():
        port = module.internal_signals[signalName]
        portString = portToString(port)
        f.write(f"{portString};\n")


def writeIODefinitions(f, module: Module):
    ports = module.getPortList()
    for portName in ports:
        port = module.getPort(portName)
        portString = portToString(port)
        f.write(f"{portString};\n")

    f.write("\n")


def writeModuleInst(f, moduleInst: ModuleInst):

    inplaceParameterString = ""
    if moduleInst.hasInplaceParameters():
        inplaceParameterList = [str(x) for x in moduleInst.getInplaceParameters()]
        inplaceParameterString = "#(" + ",".join(inplaceParameterList) + ")"

    f.write(
        f"{moduleInst.getModuleName()} {inplaceParameterString} {moduleInst.getInstName()} (\n"
    )
    portStrings = []
    if moduleInst.is_standard_inst:
        ports = moduleInst.getPortList()
        for port in ports:
            # we skip the comma for the last port
            portStrings.append(f"\t.{port} ({moduleInst.getPort(port)})")
    else:
        ports = moduleInst.getPorts()
        for port in ports:
            portStrings.append(f"\t{port}")
    f.write(",\n".join(portStrings))
    f.write("\n")
    f.write(");\n")

    parameters = moduleInst.getParameters()
    parameterStrings = []
    if moduleInst.hasParameters():
        f.write("\n")
        f.write("defparam\n")

        for key, value in parameters.items():
            parameterStrings.append(f"\t{moduleInst.getInstName()}.{key} = {value}")

        f.write(",\n".join(parameterStrings))
        f.write(";\n")

        f.write("\n")
