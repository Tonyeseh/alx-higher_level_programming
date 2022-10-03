#!/usr/bin/python3
""" Module defines a Square Class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Inheits from Rectangle Class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialises Square class

            Args:
                size (int): size of square
                x (int): x coordinate of square
                y (int): y coordinate of aquare
                id (int): id of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size attribute
            
            Args:
                value (int): size of square
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ returns the print() version of square """
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id, self.x, self.y,
                self.width)
