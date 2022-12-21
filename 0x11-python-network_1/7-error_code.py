#!/usr/bin/python3
"""
displays the body of the response to a request if status code is less than 400
display error code
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
