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
import contextlib
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

    def test_negative_args(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-9, 6)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(9, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(9, 1, -8)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(8, 2, 7, -6)

    def test_zero_as_args(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 8)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(8, 0)
        self.assertEqual(Rectangle(9, 7).x, 0)
        self.assertEqual(Rectangle(8, 6).y, 0)

class TestRectangle_area(unittest.TestCase):
    """ Unittests for testing the area method of the Rectangle class """
    def test_area_small(self):
        r = Rectangle(9, 4)
        self.assertEqual(36, r.area())

    def test_area_large(self):
        r = Rectangle(8899, 39903)
        self.assertEqual(r.area(),355096797)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(9, 7).area(9, [])


class TestRectangle_str(unittest.TestCase):
    """ Unittests for testing the __str__ method of the Rectangle Class """
    def test_two_args(self):
        r = Rectangle(3, 3)
        r_str = "[Rectangle] ({}) 0/0 - 3/3".format(r.id)
        self.assertEqual(r_str, r.__str__())
        
    def test_three_args(self):
        r = Rectangle(3, 3, 9)
        r_str = "[Rectangle] ({}) 9/0 - 3/3".format(r.id)
        self.assertEqual(r_str, r.__str__())

    def test_four_args(self):
        r = Rectangle(3, 3, 8, 1)
        r_str = "[Rectangle] ({}) 8/1 - 3/3".format(r.id)
        self.assertEqual(r_str, r.__str__())

    def test_five_args(self):
        r = Rectangle(3, 3, 8, 9, 3)
        r_str = "[Rectangle] ({}) 8/9 - 3/3".format(r.id)
        self.assertEqual(r_str, r.__str__())

    def test_args_in_str(self):
        r = Rectangle(3, 3, 8, 9, 3)
        with self.assertRaises(TypeError):
            r.__str__("figure it out")


class TestRectangle_display(unittest.TestCase):
    """ Unittests for testing the display method in Rectangle Class """
    def test_display_with_arg(self):
        r = Rectangle(9, 3)
        with self.assertRaises(TypeError):
            r.display(0, 7)

    def test_display(self):
        r = Rectangle(2, 3)
        output_str = io.StringIO()
        with contextlib.redirect_stdout(output_str):
            r.display()
        self.assertEqual(output_str.getvalue(), "##\n##\n##\n")

    def test_display_with_x_y_set(self):
        r = Rectangle(4, 3, 1, 3)
        output_str = io.StringIO()
        with contextlib.redirect_stdout(output_str):
            r.display()
        self.assertEqual(output_str.getvalue(), "\n\n\n ####\n ####\n ####\n")


class TestRectangle_update(unittest.TestCase):
    """Unittests for testing update method of the Rectangle class. """

    # Passing args
    def test_update_zero_args(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update()
        self.assertEqual("[Rectangle] (5) 3/1 - 9/5", str(r))

    def test_update_one_args(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(67)
        self.assertEqual("[Rectangle] (67) 3/1 - 9/5", str(r))

    def test_update_two_args(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(90, 23)
        self.assertEqual("[Rectangle] (90) 3/1 - 23/5", str(r))

    def test_update_three_args(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(90, 23, 88)
        self.assertEqual("[Rectangle] (90) 3/1 - 23/88", str(r))

    def test_update_four_args(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(90, 23, 88, 54)
        self.assertEqual("[Rectangle] (90) 54/1 - 23/88", str(r))


    def test_update_five_args(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(90, 23, 88, 54, 42)
        self.assertEqual("[Rectangle] (90) 54/42 - 23/88", str(r))
    
    #kwargs
    def test_update_one_kwargs(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(id=66)
        self.assertEqual("[Rectangle] (66) 3/1 - 9/5", str(r))

    def test_update_two_kwargs(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(id=66, width=78)
        self.assertEqual("[Rectangle] (66) 3/1 - 78/5", str(r))

    def test_update_three_kwargs(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(id=66, width=78, height=52)
        self.assertEqual("[Rectangle] (66) 3/1 - 78/52", str(r))

    def test_update_four_kwargs(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(id=66, width=78, height=52, x=14)
        self.assertEqual("[Rectangle] (66) 14/1 - 78/52", str(r))

    def test_update_five_kwargs(self):
        r = Rectangle(9, 5, 3, 1, 5)
        r.update(id=66, width=78, height=52, x=14, y=31)
        self.assertEqual("[Rectangle] (66) 14/31 - 78/52", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """ Unittests for testing to_dictionary method of the Rectangle class. """

    def test_to_dictionary(self):
        string = {'x': 2, 'y': 0, 'id': 5, 'width': 8, 'height': 7}
        self.assertDictEqual(string, Rectangle(8, 7, 2, 0, 5).to_dictionary())

    def test_to_dictionary_with_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(89, 78).to_dictionary("args")
