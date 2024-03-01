#!/usr/bin/python3
"""
fetches
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as reqq:
        print(reqq.headers.get('X-Request-Id'))
