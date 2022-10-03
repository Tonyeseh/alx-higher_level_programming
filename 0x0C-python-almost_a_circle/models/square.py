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

    def update(self, *args, **kwargs):
        """ Updates class Square assigns attribute to rach argument

            Args:
                *args: 1st arg - id attribute
                        2nd arg - width attribute
                        3th arg - x attribute
                        4th arg - y attribute
                 **kwargs: assigns a key/value argument to attributes.
                        if *args exist and is not empty kwargs is not used.
        """
        if args is not None and len(args) != 0:
            if args[0] is not None and type(args[0]) != int:
                raise TypeError("id must be an integer")
            self.id = args[0]
            if len(args) > 1:
                self.height = self.width = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        else:
            for k, v in kwargs.items():
                if k == "id":
                    if not isinstance(v, int):
                        raise TypeError("id must be an integer")
                    self.id = v
                elif k == "size":
                    self.height = self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """ returns the print() version of square """
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id, self.x, self.y,
                self.width)
