#!/usr/bin/python3
"""
list commits (from the most recent to oldest)
"""

from sys import argv
import requests

if __name__ == '__main__':
    req = requests.get('https://api.github.com/repos/{}/{}/comts'
                     .format(argv[2], argv[1]))
    comts = req.json()
    for commit in comts[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
