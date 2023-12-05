#!/usr/bin/python3
"""code add item"""

import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

fn = "add_item.json"
if os.path.isfile(fn):
    argvv = load_from_json_file(fn)
else:
    argvv = []
argvv.extend(sys.argv[1:])
save_to_json_file(argvv, fn)
