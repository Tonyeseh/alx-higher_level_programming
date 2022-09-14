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

    def __ne__(self, other):
        """ Defines the != comparison between Square classes """
        return (self.area() != other.area())

    def __eq__(self, other):
        """ Defines the == comparisons between Square classes """
        return (self.area() == other.area())

    def __gt__(self, other):
        """ Dfines the > comparisons between Square classes """
        return (self.area() > other.area())

    def __ge__(self, other):
        """ Defines the >= comparisons between Square classes """
        return (self.area() >= other.area())

    def __lt__(self, other):
        """ Defines the < comparison for Square classes """
        return (self.area() < other.area())

    def __le__(self, other):
        """ Defines the <= comparisons for Square classes """
        return (self.area() <= other.area())
