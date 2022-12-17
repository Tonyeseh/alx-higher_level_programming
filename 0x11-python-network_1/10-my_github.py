#!/usr/bin/python3
"""
takes your Github credentials and uses the GitHub API to display your id
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get("https://api.github.com/user", auth=(username, password))
    data = r.json()
    print(data.get("id"))
