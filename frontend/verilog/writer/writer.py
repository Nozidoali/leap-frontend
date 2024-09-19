#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-19 00:28:31
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-23 23:20:41
"""

from ..modules import *
from .headerWriter import *
from .moduleWriter import *
from .statementWriter import *

def writeDefinitions(f, netlist: Netlist):
    definitions = netlist.getDefinitions()
    for key, value in definitions.items():
        if key in ["time_unit", "time_precision"]:
            continue
        f.write(f"`define {key} {value}\n")

    if "time_unit" in definitions:
        f.write(
            f"`timescale {definitions['time_unit']} / {definitions['time_precision']}\n\n"
        )


def writeVerilogAST(module: Module, filename: str):
    assert isinstance(module, Module), "module should be an instance of Module"
    module.dfg.toGraph(filename)


def writeVerilog(netlist: Netlist, filename: str):
    assert isinstance(netlist, Netlist), "netlist should be an instance of Netlist"

    with open(filename, "w") as f:
        writeHeader(f)
        writeDefinitions(f, netlist)
        for moduleName in netlist.getModules():
            module = netlist.getModule(moduleName)
            writeModuleHeader(f, module)
            writeParameters(f, module)
            writePortDefinitions(f, module)
            f.write("\n")

            for _, moduleInst in module.submodules.items():
                writeModuleInst(f, moduleInst)

            writeModuleDFG(f, module)
            f.write("endmodule\n")
