from typing import List, Dict
from ...modules import *


def _extractEvent(assignment: List[Assignment]) -> Tuple[BNode, List[Assignment]]:
    event = None
    newAssignments: List[Assignment] = []
    for assign in assignment:
        if event is None and assign.event is not None:
            event = assign.event
        if event and assign.event != event:
            print(f"event: {event.toString()}, assign.event: {assign.event.toString()}")
            assert (
                False
            ), "Multiple events in the same assignment list are not supported"
        newAssignments.append(assign.copy().setEvent(None))
    return event, newAssignments


def assignmentsToString(assignments: List[Assignment]):
    retString = ""
    if len(assignments) == 0:
        return retString
    try:
        event, newAssignments = _extractEvent(assignments)
    except AssertionError as e:
        event = None
        newAssignments = assignments
    if event is not None:
        retString += f"{event.toString()} begin\n"
    for assignment in newAssignments:
        retString += assignmentToString(assignment)
    if event is not None:
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
        f.write(portDefsToString(portDefs, _getParamValues(module)))


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
def _getParamValues(module: Module):
    listParams = module.getPortsByType(PortType.PARAMETER)
    listLocalParams = module.getPortsByType(PortType.LOCALPARAM)
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


def moduleToString(module: Module):
    moduleString = ""
    moduleString += moduleHeaderToString(module)
    moduleString += module.getMacroString()
    moduleString += portDefsToString(module.getPorts(), _getParamValues(module))
    moduleString += "\n"

    for _, moduleInst in module.submodules.items():
        moduleString += moduleInstToString(moduleInst)

    # write assignments to the same variable in the same always block
    for var in module.var2assigns:
        # print some comments for the variable
        moduleString += f"\n/* Variable {var} */\n"
        
        assignments = []
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
                assignments.append(assign)
        moduleString += assignmentsToString(assignments)

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
