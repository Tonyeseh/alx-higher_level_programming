#!/usr/bin/python3
""" Defines a class Base """


class Base:
    """ Base class

        Args:
            __nb_objects (int): number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialises the Class Base

            Args:
                id (int): integer id
        """
        if id is not None:
            self.id = id

        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
