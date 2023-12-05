#!/usr/bin/python3
"""
append_write function
"""


def append_write(filename="", text=""):
    """
    append function
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
