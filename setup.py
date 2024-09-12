#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 23:18:14
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 23:19:18
"""

from setuptools import setup, find_packages

setup(
    name="leap",
    version="0.1.0",
    author="Hanyu Wang",
    description="Yet another extensible compiler.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(include=["leap", "leap.*"]),
)
