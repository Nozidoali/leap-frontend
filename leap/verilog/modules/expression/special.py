#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 12:33:22
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 12:40:32
"""

from enum import Enum, auto


class SOPType(Enum):
    VARIABLE = "#"
    CONCAT = "\{\}"
    FUNCTION = "$"
    ASSIGN = "="
    WIRE_NB = "<="
    WIRE = "-"
    CONST = "const"
    CONDITIONAL_ASSIGN = "?="
    CONDITIONAL = "?"
