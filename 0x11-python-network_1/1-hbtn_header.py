#!/usr/bin/python3
import urllib.request
import sys

if __name__ == "__main__"

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader('X-Request-Id')
    if x_request_id is not None:
        print("X-Request-Id:", x_request_id)
    else:
        print("No X-Request-Id header found in the response.")
