#!/usr/bin/python3
""" sends a request a URL and displays the body also handles Exceptions """

import sys
from urllib import request
import urllib.error

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as resp:
            data = resp.read()
            print(data.decode('utf-8'))

    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.status))
