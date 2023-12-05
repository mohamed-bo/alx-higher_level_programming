#!/usr/bin/python3
"""code add item"""

import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fn = "add_item.json"
try:
    jso = load_from_json_file(fn)
except FileNotFoundError:
    jso = []
for i in range(1, len(sys.argv)):
    jso.append(sys.argv[i])
save_to_json_file(jso, fn)
