#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 23:20:52
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:33:42
"""

import logging

logger = logging.getLogger(__name__)

from lark import Transformer, v_args, Tree
from ...modules import *


class DeclarationTransformer(Transformer):
    pass
