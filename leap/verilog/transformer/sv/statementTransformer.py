#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 23:20:52
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:22:01
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args, Tree
from ...modules import *

from enum import Enum, auto


class StatementTransformer(Transformer):
    def single_statement(self, items):
        if isinstance(items[0], list):
            return items[0]
        return [items[0]]

    def statement_block(self, items):
        all_items = []
        for item in items:
            if isinstance(item, list):
                all_items.extend(item)
            else:
                all_items.append(item)
        return all_items

    # statement: variable_assignment ";"
    #             | conditional_statement
    #             | case_statement
    #             | system_task
    def statement(self, items):
        # we make sure that the return value is a list
        if isinstance(items[0], list):
            return items[0]
        return [items[0]]

    # conditional_statement: if_statement else_if_statements? else_statement?
    def conditional_statement(self, items):
        # we need to flatten the list
        all_items = []
        for branches in items:
            for statement in branches:
                if isinstance(statement, list):
                    all_items.extend(statement)
                else:
                    all_items.append(statement)
        return all_items

    def if_statement(self, items):
        statements = []
        for statement in items[1]:
            logger.debug(f"statement = {statement}")
            try:
                sType, assign = statement
                if sType == "variable_assignment":
                    assign.setCondition(items[0])
                    statements.append((sType, assign))
                else:
                    statements.append(statement)
            except ValueError:
                logger.info(f"statement = {statement} is not a tuple")
        return statements

    def else_if_statements(self, items):
        statements = []
        for statement in items[1]:
            logger.debug(f"statement = {statement}")
            sType, assign = statement
            if sType == "variable_assignment":
                assign.setCondition(items[0])
                statements.append((sType, assign))
            else:
                statements.append(statement)
        return statements

    def else_statement(self, items):
        statements = []
        for statement in items[0]:
            logger.debug(f"statement = {statement}")
            sType, assign = statement
            statements.append(statement)
        return statements
