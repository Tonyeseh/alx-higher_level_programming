#!/usr/bin/python3
""" Defines class Rectangle that inherits from BaseGeometry """

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """ Initialises the Rectangle object

            Args:
                width (int): width of rectangle
                height (int): height of rectangle

            Returns:
                Nothing

        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
