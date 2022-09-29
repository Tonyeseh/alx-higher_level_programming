#!/usr/bin/python3
""" Defines ``class_to_json(obj)`` function """


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure
        (list, dictionary, string, integer, and boolean) for JSON
        serialisation of an object

        Args:
            obj (any object): instance of a Class
    """
    return (obj.__dict__)
