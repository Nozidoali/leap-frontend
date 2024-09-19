from ..modules import *

def printDefs(module: BNGraph):
    # print the definitions of the module
    for var in module.var2assigns:
        print(var)