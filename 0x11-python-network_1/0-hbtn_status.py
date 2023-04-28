#!/usr/bin/python3
import urllib.request

"""A script that
  fetches https://alx-intranet.hbtn.io/status.
  uses urlib package
"""

if __name__=='__main__':

url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as res:
        body = res.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
