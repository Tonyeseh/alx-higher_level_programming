#!/usr/bin/python3
""" Defines ``load_from_json_file(...)`` function """

""" Uses json module """
import json

def load_from_json_file(filename):
    """ creates an Object from a "JSON file"

        Args:
            filename (string): string of filename
    """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
