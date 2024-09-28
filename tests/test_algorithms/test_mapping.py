from frontend import *
import pytest


def runMapping(module: Module):
    graphOld = moduleToGraph(module)
    graphNew = technologyMapping(graphOld)
    newModule = graphToModule(graphNew)
    return newModule


# Test 01
# Mapping
@pytest.mark.skip(reason="not implemented")
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
    moduleNew = runMapping(moduleOld)
    print(moduleToString(moduleNew))


if __name__ == "__main__":
    test_01_mapping()
