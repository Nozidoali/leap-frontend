from leap import *

if __name__ == '__main__':
    netlist = readVerilog('examples/toy.v')
    writeVerilog(netlist, 'examples/toy_transformed.v')