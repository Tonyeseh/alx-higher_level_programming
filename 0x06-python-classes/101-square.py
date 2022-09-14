#!/usr/bin/python3
""" Square Class """


class Square:
    """Defines a new square object"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Gets the value of attribut size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the value of size and also validates the size.

        Args:
            size (int): The size of the new square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Getter for attribute position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter for attribute position.

        Args:
            value (tuple): position of new square
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            if self.__position[1] > 0:
                for y in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)

    def __str__(self):
        """ Defines print() format for any object Square """
        if self.__size > 0:
            y_lines = "\n" * self.__position[1]
            x_lines = " " * self.__position[0]
            square = "#" * self.__size
            line = x_lines + square
            print_s = y_lines + ((line + "\n") * (self.__size - 1)) + (line)
        else:
            print_s = ""
        return print_s
