#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 22:33:09
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-23 23:19:24
"""

from typing import List, Dict, Tuple
from ...modules import *
from .headerWriter import *

def assignmentsToString(assignments: List[Assignment]):
    retString = ""
    if len(assignments) == 0:
        return retString
    if len(assignments) == 1:
        return assignmentToString(assignments[0])
    eventTmp = None
    noConditionAssign = None
    for assign in assignments:
        if assign.condition is None:
            if noConditionAssign is not None:
                assert False, "Multiple assignments with and without conditions are not supported"    
            else:
                noConditionAssign = assign

        if assign.event is None:
            continue
        if eventTmp == None:
            eventTmp = assign.event
        elif eventTmp != assign.event:
            assert False, "Multiple events in the same assignment list are not supported"

    # reordering the assignments
    if noConditionAssign is not None:
        assignments.remove(noConditionAssign)
        assignments.append(noConditionAssign)

    if eventTmp is not None:
        retString += f"{eventTmp.toString()} begin\n"

    lenAssignments = len(assignments)
    for iAssign in range(lenAssignments):
        assign = assignments[iAssign]
        if assign.condition is not None:
            condition = assign.condition.toString()
        else:
            condition = None
        target = assign.target.toString()
        expression = assign.expression.toString()
        assignOp = "=" if assign.isBlocking else "<="
        if iAssign == 0:
            retString += f"\tif ({condition}) begin\n\t\t{target} {assignOp} {expression};\n\tend\n"
        elif iAssign == lenAssignments - 1 and noConditionAssign is not None:
            retString += f"\telse begin\n\t\t{target} {assignOp} {expression};\n\tend\n"
        else:
            retString += f"\telse if ({condition}) begin\n\t\t{target} {assignOp} {expression};\n\tend\n"

    if eventTmp is not None:
        retString += "end\n"
    
    return retString


def assignmentToString(assignment: BNEdge):
    assert isinstance(assignment, BNEdge)
    return assignment.toString()


def writeAssignment(f, assignment: Assignment):
    assignmentString = assignmentToString(assignment)
    f.write(assignmentString)


def writeAssignments(f, module: Module):
    for var in module.var2assigns:
        for assign in module.getAssignmentsOf(var):
            writeAssignment(f, assign)


def moduleHeaderToString(module: Module):
    name = module.getName()
    portString = [f"\t{port}" for port in module.getIOs()]
    return f"module {name}(\n" + ",\n".join(portString) + "\n);\n\n"


def writeModuleHeader(f, module: Module):
    headerString = moduleHeaderToString(module)
    f.write(headerString)


def portDefsToString(portDefs: Dict[str, Port], listParamValues: dict):
    retString = ""
    for _, port in portDefs.items():
        if port.name in listParamValues:
            retString += f"{portToString(port)} = {listParamValues[port.name]};\n"
        else:
            retString += portToString(port) + ";\n"
    return retString + "\n"


def writePortDefinitions(f, module: Module):
    portDefs: dict = module.getPorts()
    if len(portDefs) > 0:
        f.write(portDefsToString(portDefs, getParamValues(module)))


def moduleInstToString(moduleInst: ModuleInst):
    paramString = ""
    params = moduleInst.getParameters()
    if len(params) > 0:
        paramString = "#( "
        paramString += ",".join(
            [f".{key}({value.toString()})" for key, value in params.items()]
        )
        paramString += ") "
    portString = ""
    assignments = moduleInst.getAssignments()
    if len(assignments) > 0:
        portString += ",\n".join(
            [f".{key}({value.toString()})" for key, value in assignments]
        )

    retString = (
        f"{moduleInst.module} {paramString} {moduleInst.name} (\n{portString}\n);\n"
    )

    return retString


def writeModuleInst(f, moduleInst: ModuleInst):
    moduleInstString = moduleInstToString(moduleInst)
    f.write(moduleInstString)


# function to extract the default values of the parameters
def getParamValues(module: Module):
    listParams = [port for port in module.getPortsByType(PortType.PARAMETER)]
    listLocalParams = [port for port in module.getPortsByType(PortType.LOCALPARAM)]
    listParams += listLocalParams
    defaultParamsValues = {}
    for var in module.var2assigns:
        for assign in module.getAssignmentsOf(var):
            if assign.target.toString() in listParams:
                assert (
                    assign.expression.isConstant()
                ), f"Expected constant expression for parameters, got {assign.expression}"
                defaultParamsValues[assign.target.toString()] = (
                    assign.expression.toString()
                )
    return defaultParamsValues


def moduleToString(module: Module, inblockVar: bool = False):
    moduleString = ""
    moduleString += moduleHeaderToString(module)
    moduleString += module.getMacroString()
    moduleString += portDefsToString(module.getPorts(), getParamValues(module))
    moduleString += "\n"

    for _, moduleInst in module.submodules.items():
        moduleString += moduleInstToString(moduleInst)

    if inblockVar:
        # write assignments to the same variable in the same always block
        for var in module.var2assigns:
            assignments = []
            for assign in module.getAssignmentsOf(var):
                # TODO: consider the wire/latch/reg
                # skip the assignment if it's a parameter or localparam and it's a constant expression without condition
                skipAssignment =  (
                    assign.target.toString() in module.getPortsByType(PortType.PARAMETER) 
                    or assign.target.toString() 
                    in module.getPortsByType(PortType.LOCALPARAM) 
                    and assign.expression.isConstant() 
                    and assign.condition is None
                )
                if not skipAssignment:
                    assignments.append(assign)
            moduleString += assignmentsToString(assignments)
    else:
        for var in module.var2assigns:
            for assign in module.getAssignmentsOf(var):
                # TODO: consider the wire/latch/reg
                # skip the assignment if it's a parameter or localparam and it's a constant expression without condition
                skipAssignment = (
                    assign.target.toString() in module.getPortsByType(PortType.PARAMETER)
                    or assign.target.toString()
                    in module.getPortsByType(PortType.LOCALPARAM)
                    and assign.expression.isConstant()
                    and assign.condition is None
                )
                if not skipAssignment:
                    moduleString += assignmentToString(assign)
    moduleString += "endmodule\n"
    return moduleString


def writeModule(f, module: Module):
    writeModuleHeader(f, module)
    writePortDefinitions(f, module)
    f.write("\n")

    for _, moduleInst in module.submodules.items():
        writeModuleInst(f, moduleInst)

    writeAssignments(f, module)
    f.write("endmodule\n")
