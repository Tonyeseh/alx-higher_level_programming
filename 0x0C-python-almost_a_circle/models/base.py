#!/usr/bin/python3
""" Defines a class Base """
import json
import csv
import turtle


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
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation ``json_string``

            Args:
                json_string (json string): string representing a
                                            list of dictionaries
        """
        if json_string is None:
            return ([])
        return (json.loads(json_string))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string format representations
            of list_dictionaries

            Args:
                list_dictionaries (list of dictionaries): list of dictionaries

        """
        if list_dictionaries is None or
                list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

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
                return

        list_dict = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())

        json_str = cls.to_json_string(list_dict)

        with open(filename, "w", encoding="utf-8") as fs:
            fs.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set

            Args:
                **dictionary (pointer to dictionary):

            use update method to assign attribute after
            creating instance with dummy mandatory attributes
        """
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        else:
            new_obj = cls(1)

        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, encoding="utf-8") as f:
                json_str = f.read()
                list_dict = cls.from_json_string(json_str)
                inst_list = []
                for inst in list_dict:
                    inst_list.append(cls.create(**inst))
                return inst_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serialises class in CSV format

            Args:
                list_objs (list): list of objects

            Format:
                Rectangle: <id>,<width>,<height>,<x>,<y>
                Square: <id>,<size>,<x>,<y>
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_f:
            if list_objs is None or list_objs == []:
                csv_f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_f, fieldnames=fieldname)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classed instantiated from a csv file.

            Retuns:
                if the file does not exist - an empty list
                Otherwise a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldname = ["id", "width", "height", "x", "y"]
                else:
                    fieldname = ["id", "size", "x", "y"]
                list_dict = list(csv.DictReader(csv_file, fieldname))
                list_dict = [{k: int(v)
                             for k, v in dic.items()}
                             for dic in list_dict]
                obj_list = [cls.create(**obj) for obj in list_dict]
                return obj_list

        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Opens a window and draws all the Rectangles and
            Squares in the list
            Args:
                list_rectangles: list of rectangles
                lsit_squares: list of squares
        """
        obj = turtle.Turtle()
        obj.pensize(3)
        obj.shape("turtle")

        obj.color("teal")
        for rect in list_rectangles:
            obj.showturtle()
            obj.penup()
            obj.goto(rect.x, rect.y)
            obj.pendown()
            for i in range(2):
                obj.forward(rect.width)
                obj.left(90)
                obj.forward(rect.height)
                obj.left(90)
            obj.hideturtle()

        obj.color("brown")
        for sq in list_squares:
            obj.showturtle()
            obj.penup()
            obj.goto(sq.x, sq.y)
            obj.pendown()
            for i in range(4):
                obj.forward(sq.size)
                obj.left(90)
            obj.hideturtle()

        turtle.done()
