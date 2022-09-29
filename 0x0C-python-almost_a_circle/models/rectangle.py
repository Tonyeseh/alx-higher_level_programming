#!/usr/bin/python3
""" Defines a Rectangle class"""
from base import Base


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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        self.__y = value
