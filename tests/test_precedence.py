# Reference: https://documentation-rp-test.readthedocs.io/en/latest/tutorfpga04.html#operators-precedence

from frontend import *
import os

# change the working directory to the root directory of the project
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def getPrioritized(op1: OPType, op2: OPType) -> str:
    # Generate the Verilog string
    module = Module()
    module.setName("top")
    n1: BNode = None
    if op1.numOperands == 2:
        # create a binary operation
        module.addPort(InputPort("n1_a"))
        module.addPort(InputPort("n1_b"))
        a = VarNode("n1_a")
        b = VarNode("n1_b")
        n1 = OPNode("*", op1, a, b)

    elif op1.numOperands == 1:
        # create a unary operation
        module.addPort(InputPort("n1"))
        a = VarNode("n1")
        n1 = OPNode("*", op1, a)

    n2: BNode = None
    if op2.numOperands == 2:
        # create a binary operation
        module.addPort(InputPort("na_a"))
        a = VarNode("n2_a")
        n2 = OPNode("*", op2, n1, a)

    elif op2.numOperands == 1:
        # create a unary operation
        a = VarNode("n2")
        n2 = OPNode("*", op2, n1)

    # add the output port
    module.addPort(OutputPort("f"))
    f = VarNode("f")
    module.addAssignment(Assignment(f, n2))

    verilogStr = moduleToString(module)

    # we do a trick and remove the parathesis in the assignment
    for line in verilogStr.split("\n"):
        if "assign" in line:
            newLine = line.replace("(", "").replace(")", "")
            verilogStr = verilogStr.replace(line, newLine)
            break

    netlist = transformVerilogToNetlist(verilogStr)
    module = netlist.getModule("top")

    # we check which operator is on the top
    assign: BNode = module.getAssignNode("f")
    return assign.operation


# test 01
# corner cases are stored in the examples/verilogs/operators_precedence.v file
def test_01_cornercases():
    # netlist = readVerilog("examples/verilogs/operators_precedence.v")
    # mut1 = netlist.getModule("test1")
    # mut1.exportDOT()
    # mut1.writeDOT("test1.dot")
    tree = parseVerilogToAST(open("examples/verilogs/operators_precedence.v").read())
    print(tree.pretty())


if __name__ == "__main__":
    test_01_cornercases()
    # test_00_precedence()
