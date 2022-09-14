#!/usr/bin/python3
""" Square Class """


class Square:
    """Defines a new square object"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """ Gets the value of attribut size """
        return self.__size

    @size.setter
    def size(self, size):
        """ Sets the value of size and also validates the size.

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Calculate and Returns the area of a square object

        Args:
            None
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ Prints out in stdout the square with the character # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
