#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email":sys.argv[2]}

    data = urllib.parse.urlencode(value).encode("ascii")
    req = urllib.request.Request(url, data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
