#!/usr/bin/python3
""" Module defines  ``is_kind_of_class`` function """

def is_kind_of_class(obj, a_class):
    """ Check if an object is an instance of or the object is an instance
        of a class that inherited from, the specified class.

        Args:
            obj (object): object
            a_class (class): a class

        Return:
            True: if the object is an insance of or an instance of a class
            that inherited from, the specified class.
            False: If otherwise.

    """
    if isinstance(obj, a_class):
        return True

    else:
        return False
