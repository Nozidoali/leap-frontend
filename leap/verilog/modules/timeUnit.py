#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-07-23 20:45:03
Last Modified by: Hanyu Wang
Last Modified time: 2024-07-23 20:49:59
"""

from enum import Enum


class TimeUnit(Enum):
    fs = "fs"
    ps = "ps"
    ns = "ns"
    us = "us"
    ms = "ms"
    s = "s"

    @staticmethod
    def fromString(timeUnitStr: str):
        if timeUnitStr == "fs":
            return TimeUnit.fs
        elif timeUnitStr == "ps":
            return TimeUnit.ps
        elif timeUnitStr == "ns":
            return TimeUnit.ns
        elif timeUnitStr == "us":
            return TimeUnit.us
        elif timeUnitStr == "ms":
            return TimeUnit.ms
        elif timeUnitStr == "s":
            return TimeUnit.s
        else:
            return None

    @staticmethod
    def toString(timeUnit: "TimeUnit"):
        return timeUnit.value if timeUnit is not None else None


class TimeValue:
    def __init__(self, value: float, unit: TimeUnit) -> None:
        self.value = value
        self.unit = unit

    def __repr__(self) -> str:
        return f"{int(self.value)} {self.unit}"
