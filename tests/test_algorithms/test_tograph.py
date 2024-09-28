from frontend import *


def readAfterWrite(module: Module):
    graph = moduleToGraph(module)
    newModule = graphToModule(graph)
    print(moduleToString(newModule))
    assert module == newModule


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


if __name__ == "__main__":
    test_00_basic()
