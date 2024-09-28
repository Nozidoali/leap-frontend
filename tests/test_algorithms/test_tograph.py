from frontend import *


def readAfterWrite(module: Module):
    graph = moduleToGraph(module)
    newModule = graphToModule(graph)
    return newModule


def test_00_basic():
    verilogStr = """
module top (
    input a,
    output f
);

always @(*) begin
    if (a) begin
        f = 1;
    end else begin
        f = 0;
    end
end

endmodule
"""
    module = transformVerilogToNetlist(verilogStr).getModuleAt(0)
    readAfterWrite(module)


# Test 01
# Mapping
def test_01_mapping():
    verilogStr = """
module top (
    input a,
    output f
);

always @(*) begin
    if (a) begin
        f = 1;
    end else begin
        f = 0;
    end
end

endmodule
"""
    moduleOld = transformVerilogToNetlist(verilogStr).getModuleAt(0)
    moduleNew = readAfterWrite(moduleOld)
    print(moduleToString(moduleNew))


if __name__ == "__main__":
    test_01_mapping()
