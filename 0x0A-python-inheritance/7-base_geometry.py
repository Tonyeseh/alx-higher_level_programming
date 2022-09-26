#!/usr/bin/python3
""" Defines a BaseGeometry Class """

class BaseGeometry():
    """ Defines a class BaseGeometry based on 5-base_geometry.py"""
    
    def area(self):
        """ Raises a NameError """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value

            Args:
                name (always string): name
                value (int): value to be validated

            Raises:
                TypeError: if value is not an integer
                ValueError: if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
