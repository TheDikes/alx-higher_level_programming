#!/usr/bin/python3
"""A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response (decoded in utf-8).
"""
import sys
from urllib import request, error

if __name__ == "__main__":

    url = sys.argv[1]

    try:
        with request.urlopen(url) as res:
            body = res.read().decode('UTF-8')
            print(body)
    except error.HTTPError as er:
        print('Error code:', er.code)
