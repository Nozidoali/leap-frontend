#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 23:20:52
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:22:01
"""

from typing import List, Dict, Any, Tuple
from lark import Transformer
from ...modules import *


def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            if item is not None:
                result.append(item)
    return result


class ConditionTransformer(Transformer):
    def statement(self, items):
        statements = flatten(items)
        for statement in statements:
            assert isinstance(
                statement, Statement
            ), f"statement = {statement}, type = {type(statement)}"
        return statements

    def single_statement(self, items):
        # we make sure that the return value is a list
        return flatten(items)

    def statement_block(self, items):
        return flatten(items)

    # conditional_statement: if_statement else_if_statements? else_statement?
    def conditional_statement(
        self, items: List[Tuple[BNode, List[Statement]]]
    ) -> List[Statement]:
        allStatements = []
        currCondition = None
        for cond, statements in items:
            # process the condition
            if currCondition is None:
                condNew = cond
            else:
                condNew = OPNode("!", OPType.UNARY_NOT, currCondition)
                if cond is not None:
                    condNew = OPNode("&&", OPType.BINARY_AND, condNew, cond)
                
            # propagate the condition
            if currCondition is None:
                assert cond is not None, "condition is None"
                currCondition = cond
            else:
                currCondition = OPNode("||", OPType.BINARY_OR, currCondition, cond)

            # process the statements
            for statement in statements:
                if isinstance(statement, AssignmentStatement):
                    statement.addCondition(condNew)
                    # print(f"statement = {statement.assignment.toString()}")
                allStatements.append(statement)

        return allStatements

    def if_statement(self, items) -> Tuple[BNode, list]:
        return items

    def else_if_statement(self, items) -> Tuple[BNode, list]:
        # TODO: we need to consider the previous if statement
        return items

    def else_statement(self, items) -> Tuple[BNode, list]:
        return None, items[0]

    # case_statement: "case" "(" expression ")" case_content "endcase"
    def case_statement(self, items):
        lhs: BNode = items[0]
        caseStatements = []
        for cond, statements in items[1:]:
            condition = (
                OPNode("==", OPType.BINARY_EQ, lhs, cond) if cond is not None else None
            )
            caseStatements += [
                x.addCondition(condition)
                for x in statements
                if isinstance(x, AssignmentStatement)
            ]
        return caseStatements

    def regular_case(self, items) -> list:
        return items

    def default_case(self, items) -> list:
        return None, items[0]
