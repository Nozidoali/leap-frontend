from verilog import *


def test1():
    net = readVerilog("examples/toy.v")
    # prin the type of net
    print(type(net))
    module: Module = net.modules[0]
    module.exportDOT("examples/toy.dot")
    writeVerilog(net, "examples/toy_transformed.v")


def test2():
    net = readVerilog("examples/add2.v")
    # prin the type of net
    print(type(net))
    module: Module = net.modules[0]
    module.exportDOT("examples/add2.dot")


def test3():
    net = readVerilog("examples/add3.v")
    # prin the type of net
    print(type(net))
    module: Module = net.modules[0]
    module.exportDOT("examples/add3.dot")


def test4():
    net = readVerilog("examples/mult.v")
    # prin the type of net
    print(type(net))
    module: Module = net.modules[0]
    module.exportDOT("examples/mult.dot")


if __name__ == "__main__":
    test4()
