from frontend import *


# Test 00
# Simple graph to module
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


# Test 01
# Simple graph to module
def test_01_elaborate_if_else():
    verilogString = """
module top (
    input wire [7:0] a,
    input wire [7:0] b,
    output wire f
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
    dotNew.write("outputNew.dot")
    moduleNew = graphToModule(dotNew)
    print(moduleToString(moduleNew))

    assert moduleNew.numInputs == 2
    assert moduleNew.numOutputs == 1

    assert moduleNew.getPort("a").range == BasicRange(8)
    assert moduleNew.getPort("b").range == BasicRange(8)


# Test 02
# One run of full elaboration
def test_02_elaborate_if_else():
    verilogString = """
module top (
    input wire [1:0] a,
    input wire [1:0] b,
    output wire f
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
    dotNew = fullElaborate(dotOld)
    # dotNew = extractWindow(dotOld, "f", ["a", "b"])
    dotNew.write("outputNew.dot")
    moduleNew = graphToModule(dotNew)
    print(moduleToString(moduleNew))

    assert moduleNew.numInputs == 2, f"Expected 2, got {moduleNew.numInputs}"
    assert moduleNew.numOutputs == 1, f"Expected 1, got {moduleNew.numOutputs}"


if __name__ == "__main__":
    # test_00_elaborate_if_else()
    # test_01_elaborate_if_else()
    test_02_elaborate_if_else()
