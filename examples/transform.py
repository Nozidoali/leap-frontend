from leap import *

if __name__ == "__main__":
    net = readVerilog("examples/toy.v")
    writeVerilog(net, "examples/toy_transformed.v")
