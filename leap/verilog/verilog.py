#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-05-17 15:11:03
Last Modified by: Hanyu Wang
Last Modified time: 2024-05-17 15:21:01
"""


class Module:
    def __init__(self, lines: list = []) -> None:
        self.name = None
        self.inputs = []
        self.outputs = []
        self.wires = []
        self.assigns = []
        self.components = []
        self.lines = lines


class Verilog:
    def __init__(self, lines: list = []) -> None:
        self.top = None
        self.modules = []
        self.lines = lines

    def lower_modules(self):
        # identify the modules in the lines
        modules = []
        for line in self.lines:
            if "module" in line:
                modules.append(line)
