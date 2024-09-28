from frontend import *


def readAfterWrite(module: Module):
    graph = moduleToGraph(module)
    # graph.write("test.dot")
    newModule = graphToModule(graph)
    newGraph = moduleToGraph(newModule)
    # newGraph.write("test_new.dot")
    print(moduleToString(newModule))


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
