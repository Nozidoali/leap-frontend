#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 12:23:06
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 12:27:56
"""

from enum import Enum, auto


# unary_operator: "!"     -> unary_not
#                 | "~"   -> unary_inv
#                 | "^"   -> unary_xor // TODO: figure out what this is
#                 | "+"   -> unary_pos // Unary plus (extend as needed)
#                 | "-"   -> unary_neg // Unary minus (extend as needed)
class UOPType(Enum):
    NOT = "!"
    NEG = "-"
    POS = "+"
    INV = "~"
    XOR = "^"
    MACRO = "`"

    @staticmethod
    def fromString(op: str):
        if op == "unary_not":
            return UOPType.NOT
        elif op == "unary_neg":
            return UOPType.NEG
        elif op == "unary_pos":
            return UOPType.POS
        elif op == "unary_inv":
            return UOPType.INV
        elif op == "unary_xor":
            return UOPType.XOR
        elif op == "macro":
            return UOPType.MACRO
        else:
            raise ValueError(f"Unknown unary operator {op}")
