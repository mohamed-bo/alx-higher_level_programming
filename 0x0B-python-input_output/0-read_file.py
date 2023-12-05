#!/usr/bin/python3
"""
function read_file
"""


def read_file(filename=""):
    """
    read file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
