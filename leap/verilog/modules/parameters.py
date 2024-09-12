#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 18:22:19
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 19:03:09
"""

import logging

logger = logging.getLogger(__name__)

from .expression import *


class Parameter:
    def __init__(self, range: Range, name: str, value: str):
        logger.info(f"Parameter: {name} = {value}")
        self.name = name
        self.range = range
        self.value = value

    def __repr__(self):
        return "#{}".format(self.name, self.value)

    def getName(self):
        return self.name
