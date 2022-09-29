#!/usr/bin/python3
""" Defines class MyInt that inherits from int """


class MyInt(int):
    """ ``MyInt`` is a rebel.

        MyInt has == and != operators inverted
    """

    def __eq__(self, other_obj):
        """ Defines == operator of this class

            Args:
                other_obj (int): another obj

            Return: False if self == other_obj
                    and True otherwise
        """
        return super().__ne__(other_obj)

    def __ne__(self, other_obj):
        """ Defines != operator for this class

            Args:
                other_obj (int): another object

            Returns: True if self == other_obj
                    Otherwise, False
        """
        return super().__eq__(other_obj)
