#!/usr/bin/python3
"""
fetches
"""

if __name__ == '__main__':
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    text = req.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
