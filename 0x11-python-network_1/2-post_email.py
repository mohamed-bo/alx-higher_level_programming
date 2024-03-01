#!/usr/bin/python3

"""
takes in a URL and an email address, sends a POST request
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    mail = sys.argv[2]
    data = urllib.parse.urlencode({'email': mail})
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as res:
        print(res.read().decode('utf-8'))
