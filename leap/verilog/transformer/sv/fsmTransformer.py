#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 14:32:55
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-01 18:14:53
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args, Tree
from ...modules import *


class FSMTransformer(Transformer):
    # case_statement: "case" "(" expression ")" case_content "endcase"
    def case_statement(self, items):
        expression: DFGNode = items[0]
        assert expression.isVariable(), f"Expression is not a variable: {expression}"
        contents = items[1]

        new_assignment_statements = []
        for content in contents:
            stateNode, assignment_statements = content
            if stateNode is None:
                # add the assignments to the front of the list
                new_assignment_statements = (
                    assignment_statements + new_assignment_statements
                )
                continue

            # Add the state condition to the assignments
            additional_condition = createBinaryOpNode(
                BOPType.EQUAL, expression, stateNode
            )
            for assignment_statement in assignment_statements:
                statementType, assignment = assignment_statement
                assignment.addCondition(additional_condition)
                new_assignment_statements.append(("variable_assignment", assignment))

        return new_assignment_statements

    def case_content(self, items):
        # print(f"case_content: {items}")
        return items

    def case_item(self, items) -> list:
        state = str(items[0])

        if state == "default":
            stateNode = None
        else:
            stateNode = createVariableNode(state)

        assignment_statements = items[1]
        return stateNode, assignment_statements

    def case_label(self, items):
        return items[0]

    # ?case_action: statement_block | single_statement
    def case_action(self, items):
        return items

    def default_assignments(self, items):
        pass  # Ignore default assignments for now
