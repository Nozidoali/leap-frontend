from frontend import *

def test_00_elaborate_if_else():
    verilogString = """
module top (
    input wire a,
    input wire b,
    output reg f
);

always @(*) begin
    if (a > b) begin
        f = a;
    end else if (a < b) begin
        f = b;
    end else begin
        f = 0;
    end
end

endmodule
"""
    netlist: Netlist = transformVerilogToNetlist(verilogString)
    module = netlist.getModuleAt(0)
    dotOld = moduleToGraph(module)
    dotOld = reduce(dotOld)
    elaborateConditionsAt(dotOld, "f")
    dotNew = extractWindow(dotOld, "f", ["a", "b"])
    moduleNew = graphToModule(dotNew)
    print(moduleToString(moduleNew))
    
    assert moduleNew.numInputs == 2
    assert moduleNew.numOutputs == 1
    

if __name__ == "__main__":
    test_00_elaborate_if_else()