#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 14:59:24
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 14:59:39
"""


class FSM:
    def __init__(self) -> None:
        self.states = []
        self.transitions = {}
        self.outputs = {}
