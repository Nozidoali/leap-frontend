#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-01 13:24:16
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-01 18:45:52
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args, Tree
from ...modules import *

class EventTransformer(Transformer):
    def always_block(self, items):
        event_condition: Tree = items[0]
        statements = items[1]
        if event_condition.data == "combinational_event":
            logger.debug(f"combinational_event = {statements}")
            return statements
        if event_condition.data == "sequential_event":
            logger.debug(f"sequential_event = {statements}")
            return statements
        raise NotImplementedError

    def initial_block(self, items):
        statements = items[0]
        newStatements = []
        for statement in statements:
            try:
                varAssign: Assignment
                varAssignStr, varAssign = statement
                
                
                varAssign.addCondition
            except ValueError:
                logger.debug(f"initial_statement = {statement}")
                raise NotImplementedError
        return newStatements