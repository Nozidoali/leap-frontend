#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 23:32:17
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 23:32:23
"""

from frontend import *
import os

# change the working directory to the root directory of the project
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Test 00
# Check if the test file is correctly initialized
def test_00_Init():
    pass

# Test 01
# Parse the verilog files in the examples/verilogs folder
def test_01_Parser():
    for file in os.listdir("examples/verilogs"):
        if file.endswith(".v"):
            netlist: Netlist = readVerilog("examples/verilogs/" + file)
            assert netlist is not None, "Failed to parse " + file

