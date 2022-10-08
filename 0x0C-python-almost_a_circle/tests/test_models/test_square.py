#!/usr/bin/python3
# test_square.py
""" Defines unittests for square.py

    Unittests classes:
        TestSquare_instantiation
        TestSquare_area
        TestSquare_display
        TestSquare_update
        TestSquare_to_dictionary
        TestSquare_str
"""
import io
import sys
import unittest
import contextlib
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_square_is_base(self):
        self.assertIsInstance(Square(6, 7, 3, 1), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_args(self):
        s1 = Square(9)
        s2 = Square(8)
        self.assertEqual(s2.id, s1.id + 1)

    def test_one_args(self):
        s1 = Square(9, 5)
        s2 = Square(8, 31)
        self.assertEqual(s2.id, s1.id + 1)

    def test_three_args(self):
        s1 = Square(8, 6, 7)
        s2 = Square(2, 4, 6)
        self.assertEqual(s2.id, s1.id + 1)

    def test_four_args(self):
        s1 = Square(6, 4, 2)
        s2 = Square(8, 5, 8)
        self.assertEqual(s2.id, s1.id + 1)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(5, 3, 5, 7, 9, 9)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            Square(99, 8).__width

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            Square(7, 8, 3).__height

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            Square(9, 7, 3).__x

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            Square(7, 7).__y

    def test_width_getter(self):
        r = Square(3, 5, 6, 5)
        self.assertEqual(3, r.width)

    def test_height_getter(self):
        r = Square(3, 5, 6, 5)
        self.assertEqual(3, r.height)

    def test_x_getter(self):
        r = Square(3, 5, 6, 5)
        self.assertEqual(5, r.x)

    def test_y_getter(self):
        r = Square(3, 5, 6, 5)
        self.assertEqual(6, r.y)

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 6)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("string", 7, 8, 4)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([9, 7], 9, 8, 9)

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({'a': 1, 'b': 33})

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(8.9)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, 9.0)

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, (9, 7))

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(8, [0, "string"])

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, "string")

    def test_negative_args(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-9, 6)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(9, -8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(8, 7, -6)

    def test_zero_as_args(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 8)
        self.assertEqual(Square(9).x, 0)
        self.assertEqual(Square(8).y, 0)

class TestSquare_area(unittest.TestCase):
    """ Unittests for testing the area method of the Square class """
    def test_area_small(self):
        r = Square(9, 4)
        self.assertEqual(81, r.area())

    def test_area_large(self):
        r = Square(8899)
        self.assertEqual(r.area(), 79192201)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Square(9, 7).area(9, [])


class TestSquare_str(unittest.TestCase):
    """ Unittests for testing the __str__ method of the Square Class """
    def test_one_args(self):
        r = Square(3)
        r_str = "[Square] ({}) 0/0 - 3".format(r.id)
        self.assertEqual(r_str, r.__str__())

    def test_two_args(self):
        r = Square(3, 3)
        r_str = "[Square] ({}) 3/0 - 3".format(r.id)
        self.assertEqual(r_str, r.__str__())
        
    def test_three_args(self):
        r = Square(3, 3, 9)
        r_str = "[Square] ({}) 3/9 - 3".format(r.id)
        self.assertEqual(r_str, r.__str__())

    def test_four_args(self):
        r = Square(3, 3, 8, 1)
        r_str = "[Square] ({}) 3/8 - 3".format(r.id)
        self.assertEqual(r_str, r.__str__())

    def test_args_in_str(self):
        r = Square(3, 3, 8, 3)
        with self.assertRaises(TypeError):
            r.__str__("figure it out")


class TestSquare_display(unittest.TestCase):
    """ Unittests for testing the display method in Square Class """
    def test_display_with_arg(self):
        r = Square(9, 3)
        with self.assertRaises(TypeError):
            r.display(0, 7)

    def test_display(self):
        r = Square(2)
        output_str = io.StringIO()
        with contextlib.redirect_stdout(output_str):
            r.display()
        self.assertEqual(output_str.getvalue(), "##\n##\n")

    def test_display_with_x_y_set(self):
        r = Square(4, 3, 1, 3)
        output_str = io.StringIO()
        with contextlib.redirect_stdout(output_str):
            r.display()
        self.assertEqual(output_str.getvalue(), "\n   ####\n   ####\n   ####\n   ####\n")


class TestSquare_update(unittest.TestCase):
    """Unittests for testing update method of the Square class. """

    # Passing args
    def test_update_zero_args(self):
        r = Square(9, 5, 3, 1)
        r.update()
        self.assertEqual("[Square] (1) 5/3 - 9", str(r))

    def test_update_one_args(self):
        r = Square(9, 5, 3, 1)
        r.update(67)
        self.assertEqual("[Square] (67) 5/3 - 9", str(r))

    def test_update_two_args(self):
        r = Square(9, 5, 3, 1)
        r.update(90, 23)
        self.assertEqual("[Square] (90) 5/3 - 23", str(r))

    def test_update_three_args(self):
        r = Square(9, 5, 3, 1)
        r.update(90, 23, 88)
        self.assertEqual("[Square] (90) 88/3 - 23", str(r))

    def test_update_four_args(self):
        r = Square(9, 5, 3, 1)
        r.update(90, 23, 88, 54)
        self.assertEqual("[Square] (90) 88/54 - 23", str(r))

    #kwargs
    def test_update_one_kwargs(self):
        r = Square(9, 5, 3, 1)
        r.update(id=66)
        self.assertEqual("[Square] (66) 5/3 - 9", str(r))

    def test_update_two_kwargs(self):
        r = Square(9, 5, 3, 1)
        r.update(id=66, size=78)
        self.assertEqual("[Square] (66) 5/3 - 78", str(r))

    def test_update_three_kwargs(self):
        r = Square(9, 5, 3, 1)
        r.update(id=66, size=78, x=52)
        self.assertEqual("[Square] (66) 52/3 - 78", str(r))

    def test_update_four_kwargs(self):
        r = Square(9, 5, 3, 1)
        r.update(id=66, size=78, x=52, y=14)
        self.assertEqual("[Square] (66) 52/14 - 78", str(r))


class TestSquare_to_dictionary(unittest.TestCase):
    """ Unittests for testing to_dictionary method of the Square class. """

    def test_to_dictionary(self):
        string = {'x': 2, 'y': 0, 'id': 5, 'size': 8}
        self.assertDictEqual(string, Square(8, 2, 0, 5).to_dictionary())

    def test_to_dictionary_with_arg(self):
        with self.assertRaises(TypeError):
            Square(89, 78).to_dictionary("args")
