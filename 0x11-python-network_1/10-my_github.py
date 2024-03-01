#!/usr/bin/python3

"""Python script that takes your Github credentials (username and passw)
and uses the Github API to display your id"""

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = argv[1]
    passw = argv[2]
    res = requests.get(url, auth=(user, passw))
    print(res.json().get('id'))
