#!/usr/bin/python3
""" Defines a class Base """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string format representations
            of list_dictionaries

            Args:
                list_dictionaries (list of dictionaries): list of dictionaries

        """
        if (not isinstance(list_dictionaries, list) or
            len(list_dictionaries) == 0):
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representatin of ``list_objs`` to a file

            Args:
                list_objs (str): JSON string
        """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("[]")

        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())

        json_str = cls.to_json_string(list_dict)

        with open(filename, "w", encoding="utf-8") as fs:
            fs.write(json_str)
