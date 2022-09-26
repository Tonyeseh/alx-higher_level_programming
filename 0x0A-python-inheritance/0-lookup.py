#!/usr/bin/python3
""" Module defines ``lookup(obj)`` function. """


def lookup(obj):
    """ finds the list of available attributes and methods of an object.

    Args:
        obj (object): python object

    Returns:
        a list object.

    """
    return (dir(obj))
