from frontend import *
import pytest

def checkNodeIsAIG(node: DFGNode):
    if node.isOperation():
        assert node.operation in [
            OPType.BINARY_AND,
            OPType.UNARY_INV,
        ], f"node.operation = {node.operation} not in [OPType.BINARY_AND, OPType.UNARY_INV]"
    

def netlistIsElaborated(netlist: Netlist):
    for module in netlist.getModules():
        # check if all the assignments are composed of basic operations
        module.traverseAndApply(lambda node: checkNodeIsAIG(node))
    return True

# Test 00
# Define a module with a simple assignment
@pytest.mark.skip(reason="Not implemented")
def test_00_elaborate():
    verilogStr = """
module top(
    input a,
    output c
);
    wire [10:0] a;
    wire [2:0] i;

    wire [10:0] c;
    assign c = (a << 2) + (i + 1);
endmodule
"""
    netlist = transformVerilogToNetlist(verilogStr)
    assert netlistIsElaborated(netlist)
    
if __name__ == "__main__":
    test_00_elaborate()