#!/usr/bin/python3
""" Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """ Inherits from Base Class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialises Rectangle object

            Args:
                width (int): widhth of rectangle object
                height (int): height of rectangle object
                x (int): x-axis position of rectangle object
                y (int): y-axis position of rectangle object
                id (int): id of object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width private instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width private instance attribute

            Args:
                value (int): width of new object
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height private instance attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height private instance attribute

            Args:
                value (int): height of new object
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x private instance attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x private instance attribute

            Args:
                value (int): x of new object
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y private instance attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y private instance attribute

            Args:
                value (int): y of new object
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of a Rectangle object """
        return (self.__width * self.__height)

    def display(self):
        """ Print in stdout the Rectangle instance with the character "#" """
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print((' ' * self.__x) + ('#' * self.__width))

    def update(self, *args, **kwargs):
        """ Updates class Rectangle that assigns an atribute to each argument

            Args:
                *args: 1st arg - id attribute
                        2nd arg - width attribute
                        3rd arg - height attribute
                        4th arg - x attribute
                        5th arg - y attribute
                **kwargs: assigns a key/value argument to attributes.
                        if *args exist and is not empty kwargs is not used.
        """
        if args is not None and len(args) != 0:
            if args[0] is None or type(args[0]) != int:
                raise TypeError("id must be an integer")
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) == 5:
                self.y = args[4]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    if not isinstance(v, int):
                        raise TypeError("id must be an integer")
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
            }
        return (rect_dict)

    def __str__(self):
        """ Overrides the __str__ method and returns informationa bout object

            Format: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x,
                                                self.__y, self.__width,
                                                self.__height)
