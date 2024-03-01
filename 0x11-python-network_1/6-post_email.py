#!/usr/bin/python3

"""
takes in a URL and an email address, sends a POST request
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    mail = argv[2]
    values = {'email': mail}
    req = requests.post(url, data=values)
    print(req.text)
