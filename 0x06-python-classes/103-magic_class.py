#!/usr/bin/python3
import math
""" MagicClass Class """


class MagicClass:
    """ Defines an instance of a MagicClass object """

    def __init__(self, radius):
        """ Initializes a MagicClass object

        Args:
            radius (int or float): radius of a circle
        """
        if type(radius) is not int or type(radius) is not float:
            raise("radius must be a number")
        self.__radius = radius

    def area(self):
        """ Method finds the area of a circle """
        return (math.pi * self.__radius ** 2)

    def circumference(self):
        """ Method finds the circumference of a circle """
        return (2 * math.pi * self.__radius)
