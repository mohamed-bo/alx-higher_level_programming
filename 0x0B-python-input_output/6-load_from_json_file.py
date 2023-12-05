#!/usr/bin/python3

"""
function load from file
"""

import json


def load_from_json_file(filename):
    """
    loed json file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
