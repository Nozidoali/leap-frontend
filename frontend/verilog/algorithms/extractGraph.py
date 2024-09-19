from ..modules import *
import re


def extractGraph(graph: DotGraph, inputs: list, outputs: list, params: dict = {}):
    excludeFSM = params.get("excludeFSM", True)
    removeREG = params.get("removeREG", True)
    # extract graph from the outputs to the inputs

    # initialize a same type as graph
    newGraph = type(graph)()
    visited = set(inputs)

    fsmGraph = graph.graph.get_subgraph("cluster_fsm")
    if excludeFSM and fsmGraph is not None:
        for node in fsmGraph.nodes():
            visited.add(node.name)

    for output in outputs:
        if output not in visited:
            _extractGraphRec(graph, output, visited, newGraph)

    if removeREG:
        oldToNew = {}

        def findNewVar(var: str):
            # union find
            if var not in oldToNew or oldToNew[var] == var:
                oldToNew[var] = var
                return var
            oldToNew[var] = findNewVar(oldToNew[var])
            return oldToNew[var]

        def mergeVar(varFrom: str, varTo: str):
            # union find
            newVar1 = findNewVar(varFrom)
            newVar2 = findNewVar(varTo)
            if newVar1 != newVar2:
                oldToNew[newVar1] = newVar2

        # remove the register assignments
        assignment: Assignment
        for assignment in newGraph.assignments:
            regVar = assignment.target.name

            # we consider the following two cases:
            # 1. the reg is a pipeling register, then _reg_state<num>
            # 2. the reg is a normal register, then _reg
            if not re.match(r".*(_reg_state\d+|_reg)", regVar):
                continue

            # we get its dependencies
            deps = newGraph.getDependencies(regVar, excludeControls=True)
            assert len(deps) == 1, f"regVar: {regVar}, deps: {deps}"
            dep = deps[0]
            mergeVar(regVar, dep)

        # remove the register assignments
        for old, new in oldToNew.items():
            new = findNewVar(new)
            if old != new:
                # replace the old with the new
                for assignment in newGraph.assignments:
                    if assignment is None:
                        continue
                    assignment.replaceVariable(old, new)
                newGraph.removeVariable(old)

        newGraph.updateAssignments()
    return newGraph


def _extractGraphRec(graph: BNGraph, variable: str, visited: set, newGraph: BNGraph):
    # extract the graph recursively
    if variable in visited:
        return
    if not graph.isDefined(variable):
        return
    visited.add(variable)
    deps = graph.getDependencies(variable)
    # print(f"deps: {deps}")
    for assignment in graph.getAssignmentsOf(variable):
        # add the assignment to the new graph
        newGraph.addAssignment(assignment)
    for dep in deps:
        if dep not in visited:
            _extractGraphRec(graph, dep, visited, newGraph)
