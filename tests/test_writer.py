from frontend import *

def write_after_read(data: str):
    netlist: Netlist = transformVerilogToNetlist(data)
    newData = netlistToString(netlist)
    newNetlist: Netlist = transformVerilogToNetlist(newData)
    return netlistsAreEqual(netlist, newNetlist)

def test_00_write_assignment():
    verilogString = """
module top(
        a,
        f,
        b
);


input  a;
input  b;
output  f;


endmodule
    """
    assert write_after_read(verilogString)
    
if __name__ == "__main__":
    test_00_write_assignment()