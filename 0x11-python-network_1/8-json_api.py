#!/usr/bin/python3
"""
sends post request to http://0.0.0.0:5000/search_user
with a letter as a parameter
"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    query = ""
    if len(sys.argv) > 1:
        query = {'q': sys.argv[1]}

    r = requests.post(url, data=query)
    try:
        json = r.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json.get("id"), json.get("name")))
    except JSONDecodeError:
        print("Not a valid JSON")
