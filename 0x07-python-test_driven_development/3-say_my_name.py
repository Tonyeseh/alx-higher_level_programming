#!/usr/bin/python3
""" This module defines say_my_name function """

def say_my_name(first_name, last_name=""):
    """ Prints "My name is <first name> <last_name>"

        Args:
            first_name (string): first name
            last_name (string): last name

        Raises:
            Exception: If either or both first_name and
            last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
