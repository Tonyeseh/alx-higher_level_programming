#!/usr/bin/python3
""" This modeule defines a locked class """


class LockedClass:
    """ This class prevents user from defining new LockedClass Attributes
    except for attribute `first_name`.
    """
    __slots__ = ["first_name"]
