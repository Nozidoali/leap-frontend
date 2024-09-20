#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-28 23:18:14
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-28 23:19:18
"""

from setuptools import setup, find_packages

import os
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'frontend', '__init__.py')
    with open(version_file, 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip("'\"")

setup(
    name="frontend",
    version=get_version(),
    author="Hanyu Wang",
    description="Yet another extensible compiler.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(include=["frontend", "frontend.*"]),
)
