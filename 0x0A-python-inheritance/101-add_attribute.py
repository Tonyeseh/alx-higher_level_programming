#!/usr/bin/python3
""" Defines a function ``add_attribute(...)``"""


def add_attribute(an_obj, an_attr, a_value):
    """ Checks if ``an_attr`` of value ``a_value`` can be added to ``an_obj``

        Args:
            an_obj: object to add attribute to
            an_attr: name of the attrbute
            a_value: value of the attribue to add
    """
    if not hasattr(an_obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)

