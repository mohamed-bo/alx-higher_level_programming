#!/usr/bin/python3

"""
takes in a URL, sends a request (decoded in utf-8).
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
