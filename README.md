# LEAP Frontend

[![Gitpod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/Nozidoali/leap-compiler.git)
[![PyTest](https://github.com/Nozidoali/leap-frontend/actions/workflows/ci.yml/badge.svg)](https://github.com/Nozidoali/leap-frontend/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/leap-frontend/badge/?version=latest)](https://leap-frontend.readthedocs.io/en/latest/?badge=latest)

<img src="./static/leap-logo2.svg" width="64" height="64" align="left" style="margin-right: 24pt;margin-left: 12pt" />
LEAP (Logic nEtwork-Aware Pipelining) is a framework for exploiting logic synthesis and technology mapping to improve the performance of high-level synthesis (HLS) tools. LEAP is implemented in Python and is open-source under the MIT license. 

[Read the full documentation.](https://leap-frontend.readthedocs.io/en/latest/?badge=latest)

## Why LEAP?
**For better a HLS performance**. Conventional synthesis flows apply high-level synthesis (HLS) before logic synthesis and technology mapping, where the majority of circuit's structural and functional information are determined. Lacking these informtion, HLS algorithms such as pipelining often make suboptimal decisions that are not revertable by subsequent synthesis stages. LEAP addresses this issue by integrating logic synthesis and technology mapping into HLS, enabling HLS algorithms to make better decisions based on the circuit's structural and functional information.

## What LEAP-frontend does?

LEAP frontend:
- Takes the behavioral description of a circuit in Verilog as input.
- Transforms the behavioral description into a graph
- Apply customized **lossless** algorithms on the graph
- Write the graph into different formats for further processing in the backend

<img src="./static/leap-overview.svg" style="margin-right:12pt;margin-left: 12pt" />

## Getting Started
Install LEAP-frontend using pip:
```bash
pip install leap_frontend
```

### Usage
In Python, you can use LEAP-frontend as follows:
```python
from frontend import *

if __name__ == "__main__":
    # Read the input Verilog file
    graph = ReadVerilog("input.v")
    dot = writeDOT(graph)
    dot.write("output.dot")
```
