#!/usr/bin/python3
# test_base.py
""" Defines unittests for base.py.

    Unittests classes:
        TestBase_instantiation
        TestBase_from_json_string
        TestBase_to_json_string
        TestBase_save_to_file
        TestBase_create
        TestBase_load_from_file
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """ Unitests for testing instantiation of Base class """

    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_one_arg(self):
        self.assertEqual(13, Base(13).id)
        self.assertEqual(-9, Base(-9).id)
        self.assertEqual(987, Base(987).id)
        self.assertEqual(9.87, Base(9.87).id)
        self.assertEqual("hello", Base("hello").id)
        self.assertEqual([1, 2], Base([1, 2]).id)
        self.assertEqual({"one": 1, "two": 2}, Base({"one": 1, "two": 2}).id)
        self.assertEqual(True, Base(True).id)

    def test_id_change(self):
        b = Base(16)
        b.id = 9
        self.assertEqual(9, b.id)

    def test_type(self):
        b3 = Base()
        self.assertTrue(isinstance(b3, Base))

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(0, 6)

class TestBase_to_json_string(unittest.TestCase):
    """ Unittests for testing to_json_string method of Base class """

    def test_to_json_string_rect_type(self):
        r = Rectangle(9, 3, 1, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rect_one_dict(self):
        r = Rectangle(9, 3, 1, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 52)

    def test_to_json_string_rect_two_dicts(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(9, 8, 7, 6, 5)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 104)

    def test_to_json_string_square_type(self):
        s = Square(5, 1, 4, 8)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(5, 1, 4, 8)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 38)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(9, 8, 6, 5)
        s2 = Square(5, 1, 2, 3)
        list_dict = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dict)) == 76)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], "hello")

class TestBase_save_to_file(unittest.TestCase):
    """ Unittests for testing save_to_file method of a Base class """

    @classmethod
    def tearDown(self):
        """ Delete any created  files """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rect(self):
        r = Rectangle(9, 8, 7, 6, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) = 52)

    def test_save_to_file_two_rects(self):
        r1 = Rectangle(1, 8, 9, 4, 10)
        r2 = Rectangle(7, 9, 5, 11, 5)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 106)

    def test_save_to_file_one_square(self):
        s = Square(7, 5, 3, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_two_squares(self):
        s1 = Square(9, 8, 1, 2)
        s2 = Square(6, 7, 8, 9)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 76)

    def test_save_to_file_overwite(self):
        s = Square(9, 7, 5, 3)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

        s = Square(98, 67, 3, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 40)

    def test_save_to_file_none(self):
        Square.save_to_

if "__name__" == "__main__":
    unittest.main()
