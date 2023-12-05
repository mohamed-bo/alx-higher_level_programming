#!/usr/bin/python3
"""
function write file
"""


def write_file(filename="", text=""):
    """
    write file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
