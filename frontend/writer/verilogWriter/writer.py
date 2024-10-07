#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-19 00:28:31
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-23 23:20:41
"""

from ...modules import *
from .moduleWriter import *


def netlistToString(netlist: Netlist) -> str:
    verilogStr = ""
    verilogStr += netlist.getMacroString() + netlist.getTimescaleString() + "\n"

    for moduleName in netlist.getModuleNames():
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
    assert isinstance(netlist, Netlist) or isinstance(
        netlist, Module
    ), "netlist should be an instance of Netlist or Module"
    with open(filename, "w") as f:
        if isinstance(netlist, Module):
            f.write(moduleToString(netlist))
        else:
            f.write(netlistToString(netlist))
