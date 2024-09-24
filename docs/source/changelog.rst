Change log
==========

v0.1.4 (Not yet released)
-------------------------

* Graph Representation
    - Remove `DOTGraph` class and `ExtendedGraph` class
    - Add `exportDOT` as a separate function (not a method of `BNGraph`)

* Verilog I/O:
    - Add support for module instantiation in SystemVerilog

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
    - Add `DFGNode` class to represent nodes in a dataflow graph
    - Add `OPNode` class as a child class of `DFGNode` to represent operation nodes
    - Add `OPType` class to represent the type of operation nodes
    - Add `BNGraph` class

* Verilog I/O:
    - Update the grammar for SystemVerilog
    - Remove the support for Verilog (many features, e.g. port directions, are not lost in it's grammar)

* Algorithms:
    - Add `exportDOT` function to export a graph to a DOT file