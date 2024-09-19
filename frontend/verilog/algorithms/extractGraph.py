from ..modules import *

def extractGraph(graph: DotGraph, inputs: list, outputs: list, params: dict = {}):
    excludeFSM = params.get('excludeFSM', True)
    # extract graph from the outputs to the inputs
    
    # initialize a same type as graph
    newGraph = type(graph)()
    visited = set(inputs)
    
    fsmGraph = graph.graph.get_subgraph('cluster_fsm')
    if excludeFSM and fsmGraph is not None:
        for node in fsmGraph.nodes():
            visited.add(node.name)
    
    for output in outputs:
        if output not in visited:
            _extractGraphRec(graph, output, visited, newGraph)
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
