Change log
==========

v0.1.2 (not yet released)
-----------------------

* Graph Representation
    - Change `modules` in Netlist to a dictionary

* Verilog I/O:
    - Update writter for `port`

* Algorithms:
    - Add `netlistsAreEqual` function to compare two netlists

v0.1.0 (September 22, 2024)
-------------------------

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