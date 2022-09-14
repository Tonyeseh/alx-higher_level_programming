#!/usr/bin/python3
""" Class Square """


class Square:
    """This defines square objects
    private instance attribute: size
    """

    def __init__(self, size):
        """ Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
