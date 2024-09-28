from ..modules import *
from ..writer import *
from ..reader import *

from .exportDOT import exportDOT


def createModuleFromAssignment(assignment: Assignment, width: int = 6):
    module = Module()
    module.addAssignment(assignment)
    outVar = assignment.target.name
    outPort = OutputPort(outVar, range=Range(width - 1, 0))
    module.addPort(outPort)

    deps = module.getDependencies(outVar)
    for dep in deps:
        module.addPort(InputPort(dep, range=Range(width - 1, 0)))

    return module


def elaborateAssignment(assignment: Assignment):
    module = createModuleFromAssignment(assignment)

    # print module
    tmpFile = "tmp.v"
    writeModule(open(tmpFile, "w"), module)
    import os
    import subprocess

    # get abs path of this file's directory
    path = os.path.dirname(os.path.abspath(__file__))
    subprocess.run(f"{path}/run.sh {tmpFile} {tmpFile} top", shell=True)

    netlist = readVerilog(tmpFile)
    module = netlist.getModule("top")
    module.expandAssignment()

    graph = exportDOT(module)
    graph.write("tmp.dot")
