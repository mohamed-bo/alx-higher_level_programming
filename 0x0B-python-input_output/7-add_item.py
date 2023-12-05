#!/usr/bin/python3
"""
code add item
"""
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item(args):
    """
    add function
    """

    fn = "add_item.json"

    try:
        lis = load_from_json_file(fn)
    except FileNotFoundError:
        lis = []
    for i in range(1, len(args)):
        lis.append(args[i])
    save_to_json_file(lis, fn)


if __name__ == "__main__":
    add_item(sys.argv)
