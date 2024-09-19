#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-19 02:24:23
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-19 02:31:37
"""

import re


def flattenVerilog(inputFile: str, outputFile: str):
    with open(inputFile, "r") as f:
        lines = f.readlines()

    with open(outputFile, "w") as f:
        for line in lines:
            # we look for "[x]" and replace it with "_idx_x_"

            m = re.search(r"\[(\d+)\]", line)
            if m is not None:
                line = re.sub(r"\[(\d+)\]", r"_idx_\1_", line)

            # and we look for "." and replace it with "_dot_"
            line = re.sub(r"\.", r"_dot_", line)

            f.write(line)
