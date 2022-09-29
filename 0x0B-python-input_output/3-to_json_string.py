#!/usr/bin/python3
""" Defines ``to_json_string()`` function"""
import json


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string)

        Args:
            my_obj (any object): object to be converted
    """
    json_str = json.dumps(my_obj)
    return (json_str)
