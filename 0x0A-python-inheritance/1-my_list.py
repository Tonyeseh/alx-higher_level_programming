#!/usr/bin/python3
""" Module defines ``MyList`` class """


class MyList(list):
    """ Extention of list class

        Adds a print_sorted() function
    """

    def print_sorted(self):
        """ Prints the list but sorted(ascending sort)"""
        print(sorted(self))
