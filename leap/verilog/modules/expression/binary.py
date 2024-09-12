#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-26 03:26:04
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 12:24:21
"""

import logging

logger = logging.getLogger(__name__)

from enum import Enum, auto


# binary_operator: "+"    -> binary_add       // Addition or unary plus
#                 | "-"   -> binary_sub       // Subtraction or unary negation
#                 | "*"   -> binary_mul       // Multiplication
#                 | "/"   -> binary_div       // Division
#                 | "&&"  -> binary_and       // Logical AND
#                 | "||"  -> binary_or        // Logical OR
#                 | "&"   -> binary_bitand    // Bitwise AND
#                 | "|"   -> binary_bitor     // Bitwise OR
#                 | "^"   -> binary_xor       // Bitwise XOR
#                 | ">>"  -> binary_rshift    // Shift right
#                 | ">>>" -> binary_rshift_ext// Shift right with sign extension
#                 | "<<"  -> binary_lshift    // Shift left
#                 | "<<<" -> binary_lshift_ext// Shift left with sign extension
#                 | "%"   -> binary_mod       // Modulus
#                 | "=="  -> binary_eq        // Equal
#                 | "!="  -> binary_neq       // Not equal
#                 | "<"   -> binary_lt        // Less than
#                 | ">"   -> binary_gt        // Greater than
#                 | "<="  -> binary_leq       // Less than or equal
#                 | ">="  -> binary_geq       // Greater than or equal
#                 | "===" -> binary_eq_ext    // Case equality
#                 | "!==" -> binary_neq_ext   // Case inequality
class BOPType(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "*"
    DIV = "/"
    AND = "&&"
    OR = "||"
    BITAND = "&"
    BITOR = "|"
    XOR = "^"
    RSHIFT = ">>"
    RSHIFT_EXT = ">>>"
    LSHIFT = "<<"
    LSHIFT_EXT = "<<<"
    MOD = "%"

    EQUAL = "=="
    NEQ = "!="
    LT = "<"
    GT = ">"
    LEQ = "<="
    GEQ = ">="
    EQ_EXT = "==="
    NEQ_EXT = "!=="

    @staticmethod
    def fromString(op: str):
        if op == "binary_add":
            return BOPType.ADD
        elif op == "binary_sub":
            return BOPType.SUB
        elif op == "binary_mul":
            return BOPType.MUL
        elif op == "binary_div":
            return BOPType.DIV
        elif op == "binary_and":
            return BOPType.AND
        elif op == "binary_or":
            return BOPType.OR
        elif op == "binary_bitand":
            return BOPType.BITAND
        elif op == "binary_bitor":
            return BOPType.BITOR
        elif op == "binary_xor":
            return BOPType.XOR
        elif op == "binary_rshift":
            return BOPType.RSHIFT
        elif op == "binary_rshift_ext":
            return BOPType.RSHIFT_EXT
        elif op == "binary_lshift":
            return BOPType.LSHIFT
        elif op == "binary_lshift_ext":
            return BOPType.LSHIFT_EXT
        elif op == "binary_mod":
            return BOPType.MOD
        elif op == "binary_eq":
            return BOPType.EQUAL
        elif op == "binary_neq":
            return BOPType.NEQ
        elif op == "binary_lt":
            return BOPType.LT
        elif op == "binary_gt":
            return BOPType.GT
        elif op == "binary_leq":
            return BOPType.LEQ
        elif op == "binary_geq":
            return BOPType.GEQ
        elif op == "binary_eq_ext":
            return BOPType.EQ_EXT
        elif op == "binary_neq_ext":
            return BOPType.NEQ_EXT
        else:
            logger.error(f"Unknown operator {op}")
            raise ValueError(f"Unknown operator {op}")
