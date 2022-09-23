#!/usr/bin/python3
""" Defines a print square function """


def print_square(size):
    """ Prints a square of size "size" with '#'

        Args:
            size (int): size of square

        Raises:
            TypeError: If size is not an integer
            TypeError: If size is a float or/and is less than 0
            TypeError: If no arguments are passed
            ValueError: If size is less than 0
    """

    if (not isinstance(size, int)):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size > 0:
        for i in range(size):
            print("#" * size)
