#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 23:02:11
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-24 02:14:45
"""

from ..modules import *


def assignmentToString(assignment: Assignment):
    target = assignment.target.toString()
    expression = assignment.expression.toString()
    condition = assignment.condition

    # TODO: consider wire/latch/reg
    if condition is not None:
        condition = condition.toString()
        return f"{target} = {expression} ({condition})"
    return f"{target} = {expression}"


def writeAssignment(f, assignment: Assignment):
    target = assignment.target
    expression = assignment.expression
    condition = assignment.condition

    # TODO: consider wire/latch/reg
    f.write("always @(*) begin\n")
    if condition is not None:
        f.write(f"if ({condition}) begin\n")
    f.write(f"\t{target} = {expression};\n")
    if condition is not None:
        f.write("end\n")
    f.write("end\n\n")


def writeAssignments(f, module: Module):
    for var in module.var2assigns:
        for assign in module.getAssignmentsOf(var):
            writeAssignment(f, assign)


def writeModuleDFG(f, module: Module):
    dfg = module.getDFG()
    for node in dfg.getNodes():
        if not node.isVariable:
            continue
        if not node.hasChildren:
            continue

        variableName = node.label
        nodeType = module.getVariableType(node.label)

        # TODO: this could be done more elegantly
        lhs = VariableNode(variableName)
        if node.range is not None:
            lhs.setRange(node.range)

        assert (
            variableName in module.node_is_blocking
        ), f"node {node.label} in module {module.module_name} is not in module.node_is_blocking"
        isBlocking = module.node_is_blocking[variableName]

        children = [dfg.getNode(child) for child in node.children]

        if nodeType == "reg":
            if isBlocking:
                f.write("always @(*) begin\n")
            else:
                f.write("always @(posedge clk) begin\n")

        hasIf: bool = False
        for child in children:
            childType = child.op

            if childType == SOPType.ASSIGN:
                assert (
                    len(child.children) == 1
                ), f"node {child.label} in module {module.module_name} has more than one child: {child.children}"

                if hasIf:
                    f.write("else begin\n")

                childExpression = dfg.extractNodeHelper(child.children[0]).toString()
                if nodeType == "reg":
                    if isBlocking:
                        f.write(f"\t{lhs} = {childExpression};\n")
                    else:
                        f.write(f"\t{lhs} <= {childExpression};\n")
                else:
                    f.write(f"assign {lhs} = {childExpression};\n\n")

                if hasIf:
                    f.write("end\n")

                continue
            if childType == SOPType.CONDITIONAL_ASSIGN:
                assert (
                    len(child.children) == 2
                ), f"node {child.label} in module {module.module_name} has more than two children: {child.children}"

                ifString = "if" if not hasIf else "else if"

                # this means that we have an if statement
                hasIf = True

                condition = dfg.extractNodeHelper(child.children[0]).toString()
                trueExpression = dfg.extractNodeHelper(child.children[1]).toString()

                f.write(f"{ifString} ({condition}) begin\n")
                if nodeType == "reg":
                    if isBlocking:
                        f.write(f"\t{lhs} = {trueExpression};\n")
                    else:
                        f.write(f"\t{lhs} <= {trueExpression};\n")
                else:
                    assert isinstance(
                        lhs, str
                    ), f"variableName's type is {type(variableName)}"
                    f.write(f"\tassign {lhs} = {trueExpression};\n\n")
                f.write("end\n")

        if nodeType == "reg":
            f.write("end\n")

        assert (
            node.op == SOPType.VARIABLE
        ), f"node {node.label} in module {module.module_name} is not a variable"
