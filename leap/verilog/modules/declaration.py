#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-25 23:24:29
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-25 23:30:26
"""


class Declaration:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return "({})".format(self.name)
