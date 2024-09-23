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

def netlistToString(netlist: Netlist) -> str:
    verilogStr = ""
    definitions = netlist.getDefinitions()
    for key, value in definitions.items():
        if key in ["time_unit", "time_precision"]:
            continue
        verilogStr += f"`define {key} {value}\n"

    if "time_unit" in definitions:
        verilogStr += f"`timescale {definitions['time_unit']} / {definitions['time_precision']}\n\n"

    for moduleName in netlist.getModules():
        module = netlist.getModule(moduleName)
        verilogStr += moduleToString(module) + "\n"

    return verilogStr

def writeVerilog(netlist: Netlist | Module, filename: str):
    """
    Write the netlist to a verilog file

    :param netlist: the netlist or module to write
    :type netlist: Netlist | Module
    :param filename: the name of the file to write
    :type filename: str

    .. note::
        The input can be either a netlist or a module

    Example usage:

    .. code-block:: python

        netlist = readVerilog("path/to/verilog/file.v")
        writeVerilog(netlist, "path/to/output/file.v")

    .. seealso::

        Related functions: :func:`readVerilog`
    """
    if isinstance(netlist, Module):
        writeModule(netlist)
        return

    with open(filename, "w") as f:
        writeHeader(f)
        writeDefinitions(f, netlist)
        for moduleName in netlist.getModules():
            module = netlist.getModule(moduleName)
            writeModule(module)
