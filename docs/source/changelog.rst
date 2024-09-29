Change log
==========

v0.1.6 (Not Yet Released)
-------------------------

* Graph Representation
    - Update class name `DFGNode` to `BNode`, to separate the class from the CDFG
    - Add test cases for syntax checking 

* Verilog I/O:
    - Add condition propagation for the if else statement

v0.1.4 (September 27, 2024)
---------------------------

* Graph Representation
    - Remove `DOTGraph` class and `ExtendedGraph` class
    - Add `exportDOT` as a separate function (not a method of `BNGraph`)

* Verilog I/O:
    - Add support for module instantiation in SystemVerilog
    - Add syntax checking for port type, directions, and ranges (as well as the test cases, see: `test/test_ports.py` and `test/test_ports_false.py`). 
    - Update many classes to `dataclass` (e.g. `Port`, `Module`, `Netlist`, `Assignment`, `BNode`, `OPNode`, `OPType`, `BNGraph`) to make them immutable

v0.1.2 (September 22, 2024)
---------------------------

* Graph Representation
    - Change `modules` in Netlist to a dictionary
    - Change macros and timescale definitions into statements

* Verilog I/O:
    - Update writter for `port`

* Algorithms:
    - Add `__eq__` function to compare two netlists

v0.1.0 (September 22, 2024)
---------------------------

* Graph Representation
    - Add `BNode` class to represent nodes in a dataflow graph
    - Add `OPNode` class as a child class of `BNode` to represent operation nodes
    - Add `OPType` class to represent the type of operation nodes
    - Add `BNGraph` class

* Verilog I/O:
    - Update the grammar for SystemVerilog
    - Remove the support for Verilog (many features, e.g. port directions, are not lost in it's grammar)

* Algorithms:
    - Add `exportDOT` function to export a graph to a DOT file