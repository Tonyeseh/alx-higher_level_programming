#!/usr/bin/python3
"""
sends POST request to a URL with email a param and displays the response body
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}

    r = requests.post(url, data=email)
    print(r.text)
