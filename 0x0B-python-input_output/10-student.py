#!/usr/bin/python3
""" Defines a class Student """

class Student:
    """ Defines class Student """
    def __init__(self, first_name, last_name, age):
        """ Initialisation of Student object

            Args:
                first_name (str): first name
                last_name (str): last name
                age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dictionary representation of a Student instance """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

        return self.__dict__
