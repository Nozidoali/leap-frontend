#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2024-06-24 13:02:55
Last Modified by: Hanyu Wang
Last Modified time: 2024-06-24 14:05:19
"""

import logging
import traceback
import os


def run_with_logger(logFile: str):
    """
    run_with_logger:
        A decorator to log the function call

    :param func: the function to be decorated
    :type func: function
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            os.remove(logFile) if os.path.exists(logFile) else None
            logging.basicConfig(filename=logFile, level=logging.INFO)
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s\n - %(message)s\n\tFile "%(filename)s", line %(lineno)d\n'
            )
            logging.getLogger().handlers[0].setFormatter(formatter)

            try:
                func(*args, **kwargs)
            except Exception as e:
                logging.getLogger().error(f"Error: {e}")
                # get more information about the error
                logging.getLogger().error(traceback.format_exc())
                print(f"Failed on {args[0]}, check log file: {logFile}")
                exit(1)

        return wrapper

    return decorator
