#!/usr/bin/python3
"""
takes in a URL, sends a request
"""

import urllib.request as request
from sys import argv

if __name__ == "__main__":
    reque = request.Request(argv[1])
    with request.urlopen(reque) as reeq:
        print(reeq.headers.get('X-Request-Id'))
