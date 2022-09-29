#!/usr/bin/python3
""" Defines ``save_to_json(...)`` function """
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using JSON representation

        Args:
            my_obj (object): preferrable serialisable object
            filename (string): file to dump the JSON string
    """
    with open(filename, "w", encoding="utf-8") as f:
        json_string = json.dumps(my_obj)
        f.write(json_string)
