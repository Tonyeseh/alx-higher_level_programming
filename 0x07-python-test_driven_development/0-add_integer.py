#!/usr/bin/python3
""" This module defines an integer addtion function """

def add_integer(a, b=98):
    """ Return the sum 2 integer or float values

        Both a and b are typecasted to int before summation is done

        Raises:
            TypeError: if either a or b is not a float or integer

        Args:
            a (int or float): first number
            b (int or float): second number
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
