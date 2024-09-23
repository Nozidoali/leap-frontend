from ..modules import *


def netlistsAreEqual(
    netlist1: Netlist, netlist2: Netlist, verbose: bool = True
) -> bool:
    if len(netlist1.getModules()) != len(netlist2.getModules()):
        print(
            f"Number of modules are not equal: {len(netlist1.getModules())} != {len(netlist2.getModules())}"
        )
        return False
    # compare modules
    for module in netlist1.getModules():
        if module not in netlist2.getModules():
            print(f"Module {module} not found in netlist2")
            print(f"Modules in netlist1: {netlist1.getModules()}")
            print(f"Modules in netlist2: {netlist2.getModules()}")
            return False
        if not modulesAreEqual(
            netlist1.getModule(module), netlist2.getModule(module), verbose
        ):
            print(
                f"Module {module} in netlist1 is not equal to module {module} in netlist2"
            )
            return False
    return True


def modulesAreEqual(module1: Module, module2: Module, verbose: bool = True) -> bool:
    if module1.getName() != module2.getName():
        print(f"Module names are not equal: {module1.getName()} != {module2.getName()}")
        return False
    # compare ports
    for port in module1.getPortNames():
        if port not in module2.getPortNames():
            print(f"Port {port} not found in module {module2.getName()}")
            print(f"Ports in module {module1.getName()}: {module1.getPortNames()}")
            return False
        if module1.getPort(port) != module2.getPort(port):
            print(
                f"Port {port} in module {module1.getName()} is not equal to port {port} in module {module2.getName()}"
            )
            return False
    # compare assignments
    for var in module1.getVariableNames():
        if var not in module2.getVariableNames():
            print(f"Variable {var} not found in module {module2.getName()}")
            print(f"Variables in module {module1.getName()}: {module1.getVariableNames()}")
            return False
        assignments1 = module1.getAssignmentsOf(var)
        assignments2 = module2.getAssignmentsOf(var)
        assert len(assignments1) == len(assignments2)
        for i in range(len(assignments1)):
            print(assignments1[i])
            print(assignments2[i])
            if assignments1[i] != assignments2[i]:
                print(
                    f"Assignment {assignments1[i]} in module {module1.getName()} is not equal to assignment {assignments2[i]} in module {module2.getName()}"
                )
                return False
    
    return True
