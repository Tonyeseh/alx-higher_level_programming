#!/usr/bin/python3
""" Defines a Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inherits from Rectangle class """

    def __init__(self, size):
        """ Initialises a new Square

            Args:
                size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Print() format for a Square object """
        return ("[{}] {}/{}"
                .format(type(self).__name__, self.__size, self.__size))
