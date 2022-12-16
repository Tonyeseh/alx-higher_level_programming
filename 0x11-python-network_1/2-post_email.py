#!/usr/bin/python3
"""sends a POST request passed with an email parameter"""

import sys, urllib.request, urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    email = urllib.parse.urlencode(values)
    email = email.encode("ascii")
    req = urllib.request.Request(url, email)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
