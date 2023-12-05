#!/usr/bin/python3
"""
function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after function
    """

    line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            line += [line]
            if line.find(search_string) != -1:
                line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(line))
