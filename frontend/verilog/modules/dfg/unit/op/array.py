#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-01 18:49:04
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-01 18:50:17
"""

from enum import Enum, auto


class AOPType(Enum):
    SLICE = "[:]"
    INDEX = "[]"
