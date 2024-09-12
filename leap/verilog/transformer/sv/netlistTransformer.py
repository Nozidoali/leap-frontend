#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 20:39:14
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-23 20:39:49
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args, Tree
from ...modules import *


class NetlistTransformer(Transformer):
    def netlist(self, items):
        return Netlist(items)
