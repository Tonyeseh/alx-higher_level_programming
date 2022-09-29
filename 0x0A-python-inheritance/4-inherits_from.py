#!/usr/bin/python3
""" Module defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """ Checks if an object is a inherited instance of a class.

        Args:
            obj (any): Object
            a_class (type): class type.

        Returns:
            If obj is an inherited instance of a_class - True
            Otherwise - False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
