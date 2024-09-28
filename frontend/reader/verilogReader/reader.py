#
# Copyright (c) 2018-2021 T. {Benz,Kramer}.
#
# This file is part of verilog-parser
# (see https://codeberg.org/tok/py-verilog-parser).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from lark import Lark

# http://www.verilog.com/VerilogBNF.html
# http://www.externsoft.ch/download/verilog.html

from ...modules import *
from .verilogTransformer import VerilogTransformer

GRAMMAR_FILE = "grammar_systemverilog.lark"


def transformVerilogToNetlist(data: str) -> Netlist:
    """
    Parse a string containing data of a verilog file.
    :param data: Raw verilog string.
    :return:
    """
    ast = parseVerilogToAST(data)

    # select the transformer
    transformer = VerilogTransformer()
    netlist: Netlist = transformer.transform(ast)
    netlist.postProcess()

    return netlist


def parseVerilogToAST(data: str) -> Netlist:
    import os

    curr_dir = os.path.dirname(os.path.abspath(__file__))
    grammar_file = os.path.join(curr_dir, GRAMMAR_FILE)
    with open(grammar_file, "r") as f:
        verilog_netlist_grammar = f.read()

    parser = Lark(verilog_netlist_grammar, parser="earley", lexer="dynamic_complete")
    parseTree = parser.parse(data)

    # return the netlist
    return parseTree


# reference: https://codeberg.org/tok/py-verilog-parser/src/branch/master/verilog_parser/parser.py
def readVerilog(filename: str) -> Netlist:
    """Read the verilog from a file and return the netlist.

    :param filename: the name of the file to read
    :type filename: str
    :raises FileNotFoundError: if the file does not exist
    :return: the netlist
    :rtype: Netlist
    """
    import os

    if not os.path.exists(filename):
        raise FileNotFoundError(f"file {filename} not found")
    with open(filename, "r") as f:
        data = f.read()
    return transformVerilogToNetlist(data)
