#!/usr/bin/python3
# test_rectangle.py
""" Defines unittests for rectangle.py

    Unittests classes:
        TestRectangle_instantiation
        TestRectangle_area
        TestRectangle_display
        TestRectangle_update
        TestRectangle_to_dictionary
        TestRectangle_str
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(9, 6, 7, 3, 1), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(8)

    def test_two_args(self):
        r1 = Rectangle(9, 7)
        r2 = Rectangle(8, 6)
        self.assertEqual(r2.id, r1.id + 1)

    def test_three_args(self):
        r1 = Rectangle(8, 6, 7)
        r2 = Rectangle(2, 4, 6)
        self.assertEqual(r2.id, r1.id + 1)

    def test_four_args(self):
        r1 = Rectangle(6, 4, 2, 7)
        r2 = Rectangle(8, 5, 3, 1)
        self.assertEqual(r2.id, r1.id + 1)

    def test_five_args(self):
        self.assertEqual(Rectangle(8, 5, 3, 1, 6).id, 6)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 3, 5, 7, 9, 9)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(99, 8).__width

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(7, 8, 3).__height

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(9, 7, 3, 1, 2).__x

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            Rectangle(7, 7).__y

    def test_width_getter(self):
        r = Rectangle(3, 5, 4, 6, 5)
        self.assertEqual(3, r.width)

    def test_height_getter(self):
        r = Rectangle(3, 5, 4, 6, 5)
        self.assertEqual(5, r.height)

    def test_x_getter(self):
        r = Rectangle(3, 5, 4, 6, 5)
        self.assertEqual(4, r.x)

    def test_y_getter(self):
        r = Rectangle(3, 5, 4, 6, 5)
        self.assertEqual(6, r.y)

    def test_width_setter(self):
        r = Rectangle(3, 5, 4, 6, 5)
        r.width = 9
        self.assertEqual(r.width, 9)

    def test_height_setter(self):
        r = Rectangle(3, 5, 4, 6, 5)
        r.height = 17
        self.assertEqual(r.height, 17)

    def test_x_setter(self):
        r = Rectangle(3, 5, 4, 6, 5)
        r.x = 12
        self.assertEqual(r.x, 12)

    def test_y_setter(self):
        r = Rectangle(3, 5, 4, 6, 5)
        r.y = 8
        self.assertEqual(r.y, 8)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 6)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("string", 7, 8, 4)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([9, 7], 9, 8, 9)

    def test_none_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, None)

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(8, {'a': 1, 'b': 33})

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 8.9)

    def test_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, 9.0)

    def test_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 9, (9, 7))

    def test_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(8, 8, 9, [0, "string"])

    def test_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 8, 7, "string")
