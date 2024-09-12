#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 14:13:34
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 14:20:00
"""

from typing import List, Union, Tuple
from .verilogNumber import Number, Range

# class PortConnection:
#
#     def __init__(self, port_name: str, signal_name: str):
#         self.port_name = port_name
#         self.signal_name = signal_name
#
#     def __repr__(self):
#         return ".{}({})".format(self.port_name, self.signal_name)


class Identifier:
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return self.name


class IdentifierIndexed:
    def __init__(self, name: str, index):
        self.name = name
        self.index = index

    def __repr__(self):
        return "{}[{}]".format(self.name, self.index)


class IdentifierSliced:
    def __init__(self, name: str, range: Range):
        self.name = name
        self.range = range

    def __repr__(self):
        return "{}{}".format(self.name, self.range)


class Concatenation:
    def __init__(
        self, elements: List[Union[Identifier, IdentifierIndexed, IdentifierSliced]]
    ):
        self.elements = elements

    def __repr__(self):
        return "Concatenation()".format(", ".join([str(e) for e in self.elements]))


class ContinuousAssign:
    def __init__(self, assignments: List[Tuple[str, str]]):
        assert isinstance(assignments, list)
        self.assignments = assignments

    def __repr__(self):
        return "ContinuousAssign({})".format(
            ", ".join(("{} = {}".format(l, r) for l, r in self.assignments))
        )
