#!/usr/bin/python3
""" Module defines  ``is_same_class`` function """


def is_same_class(obj, a_class):
    """ Returns True if an object is exactly an instance of a specified
        class; otherwise False.

        Args:
            obj (object): object
            a_class (class): a class

    """
    if type(obj) == a_class:
        return True

    else:
        return False
