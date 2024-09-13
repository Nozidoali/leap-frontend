from verilog import *

if __name__ == '__main__':
    net = readVerilog('examples/toy.v')
    # prin the type of net
    print(type(net))
    writeVerilog(net, 'examples/toy_transformed.v')