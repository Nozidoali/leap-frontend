#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 22:33:09
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-23 23:19:24
"""

from ..modules import *
from .headerWriter import *
from .dfgWriter import *


def writeModuleHeader(f, module: Module):
    name = module.getName()
    f.write(f"module {name}\n")
    f.write("(\n")
    portString = [f"\t{port}" for port in module.getIOs()]
    f.write(",\n".join(portString))
    f.write("\n);\n\n")

def writeParameters(f, module: Module):
    parameters: dict = module.getParameters()

    for _, value in parameters.items():
        parameter: Parameter = value
        rangeString = f"{rangeToString(parameter.range)} " if parameter.range is not None else ""
        f.write(f"parameter {rangeString}{parameter.name} = {parameter.value};\n")

    f.write("\n")


def writePortDefinitions(f, module: Module):
    ports = module.getPorts()
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
