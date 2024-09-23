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


def moduleHeaderToString(module: Module):
    name = module.getName()
    portString = [f"\t{port}" for port in module.getIOs()]
    return f"module {name}(\n" + ",\n".join(portString) + "\n);\n\n"


def writeModuleHeader(f, module: Module):
    headerString = moduleHeaderToString(module)
    f.write(headerString)


def parametersToString(parameters: dict):
    retString = ""
    for _, parameter in parameters.items():
        rangeString = rangeToString(parameter.range)
        retString += f"parameter {rangeString}{parameter.name} = {parameter.value};\n"
    return retString + "\n"


def writeParameters(f, module: Module):
    parameters: dict = module.getParameters()
    if len(parameters) > 0:
        f.write(parametersToString(parameters))


def portDefsToString(portDefs: dict):
    retString = ""
    for _, port in portDefs.items():
        retString += portToString(port) + ";\n"
    return retString + "\n"


def writePortDefinitions(f, module: Module):
    portDefs: dict = module.getPorts()
    if len(portDefs) > 0:
        f.write(portDefsToString(portDefs))


def moduleInstToString(moduleInst: ModuleInst):
    inplaceParameterString = ""
    if moduleInst.hasInplaceParameters():
        inplaceParameterList = [str(x) for x in moduleInst.getInplaceParameters()]
        inplaceParameterString = "#(" + ",".join(inplaceParameterList) + ")"

    retString = f"{moduleInst.getModuleName()} {inplaceParameterString} {moduleInst.getInstName()} (\n"
    portStrings = []
    if moduleInst.is_standard_inst:
        ports = moduleInst.getPortList()
        for port in ports:
            # we skip the comma for the last port
            portStrings.append(f"\t.{port} ({moduleInst.getPort(port)})")
    else:
        ports = moduleInst.getPortNames()
        for port in ports:
            portStrings.append(f"\t{port}")
    retString += ",\n".join(portStrings) + "\n"
    retString += ");\n"

    parameters = moduleInst.getParameters()
    parameterStrings = []
    if moduleInst.hasParameters():
        retString += "\n"
        retString += "defparam\n"

        for key, value in parameters.items():
            parameterStrings.append(f"\t{moduleInst.getInstName()}.{key} = {value}")

        retString += ",\n".join(parameterStrings) + ";\n"

        retString += "\n"
    return retString


def writeModuleInst(f, moduleInst: ModuleInst):
    moduleInstString = moduleInstToString(moduleInst)
    f.write(moduleInstString)


def moduleToString(module: Module):
    moduleString = ""
    moduleString += moduleHeaderToString(module)
    moduleString += module.getMacroString()
    moduleString += parametersToString(module.getParameters())
    moduleString += portDefsToString(module.getPorts())
    moduleString += "\n"

    for _, moduleInst in module.submodules.items():
        moduleString += moduleInstToString(moduleInst)

    for var in module.var2assigns:
        for assign in module.getAssignmentsOf(var):
            # TODO: consider the wire/latch/reg
            moduleString += assignmentToString(assign)
    moduleString += "endmodule\n"
    return moduleString


def writeModule(f, module: Module):
    writeModuleHeader(f, module)
    writeParameters(f, module)
    writePortDefinitions(f, module)
    f.write("\n")

    for _, moduleInst in module.submodules.items():
        writeModuleInst(f, moduleInst)

    writeAssignments(f, module)
    f.write("endmodule\n")
