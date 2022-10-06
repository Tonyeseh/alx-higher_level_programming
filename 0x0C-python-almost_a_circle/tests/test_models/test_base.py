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

    def test_assigning_ID(self):
        b3 = Base()
        b4 = Base()
        self.assertEqual(b3.id + 1, b4.id)

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
        b5 = Base()
        self.assertTrue(isinstance(b5, Base))

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

class TestBase_from_json_string(unittest.TestCase):
    """ Unittests for testing from_json_string of Base class """

    def test_from_json_string_type(self):
        lst = Base.from_json_string('[{"id": 89}]')
        self.assertTrue(type(lst) == list)

    def test_from_json_string_one_obj(self):
        r = Rectangle(9, 8, 7, 6, 5)
        r_lst = [r.to_dictionary()]
        from_json = Rectangle.from_json_string(Rectangle.to_json_string(r_lst))
        self.assertEqual(r_lst, from_json)

        s = Square(9, 7, 5, 2)
        s_lst = [s.to_dictionary()]
        from_json = Square.from_json_string(Square.to_json_string(s_lst))

    def test_from_json_string_two_objs(self):
        r1 = Rectangle(8, 6, 5, 4, 3)
        r2 = Rectangle(1, 2, 3, 4, 5)
        r_lst = [r1.to_dictionary(), r2.to_dictionary()]
        from_json = Rectangle.from_json_string(Rectangle.to_json_string(r_lst))
        self.assertEqual(r_lst, from_json)

        s1 = Square(9, 8, 1, 2)
        s2 = Square(8, 5, 3, 1)
        s_lst = [s1.to_dictionary(), s2.to_dictionary()]
        from_json = Square.from_json_string(Square.to_json_string(s_lst))

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], [])

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
            self.assertTrue(len(f.read()) == 52)

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
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

class TestBase_create(unittest.TestCase):
    """ Unittests for testing create method of Base Class """

    def test_create_rectangle(self):
        r1 = Rectangle(9, 8, 7, 5, 4)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertEqual("[Rectangle] (4) 7/5 - 9/8", str(r1))
        self.assertEqual("[Rectangle] (4) 7/5 - 9/8", str(r2))

    def test_create_square(self):
        s1 = Square(9, 4, 1, 9)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertEqual("[Square] (9) 4/1 - 9", str(s1))
        self.assertEqual("[Square] (9) 4/1 - 9", str(s2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(9, 8, 7, 5, 4)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(9, 8, 7, 5, 4)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_create_square_is(self):
        s1 = Square(9, 4, 1, 9)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(9, 4, 1, 9)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """ Unittests for testing load_from_file_method of Base class """

    @classmethod
    def tearDown(self):
        """ Delete any files created. """

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except:
            pass

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(9, 6, 2, 6, 3)
        r2 = Rectangle(2, 6, 8, 1, 9)
        Rectangle.save_to_file([r1, r2])
        from_file = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(from_file[0]))
        self.assertEqual(str(r2), str(from_file[1]))

    def test_load_from_file_rectangle_type(self):
        r1 = Rectangle(9, 6, 2, 6, 3)
        r2 = Rectangle(2, 6, 8, 1, 9)
        Rectangle.save_to_file([r1, r2])
        from_file = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in from_file))

    def test_load_from_file_square(self):
        s1 = Square(7, 4, 1, 6)
        s2 = Square(8, 4, 1, 5)
        Square.save_to_file([s1, s2])
        from_file = Square.load_from_file()
        self.assertEqual(str(s1), str(from_file[0]))
        self.assertEqual(str(s2), str(from_file[1]))

    def test_load_from_file_square_type(self):
        s1 = Square(7, 4, 1, 6)
        s2 = Square(8, 4, 1, 5)
        Square.save_to_file([s1, s2])
        from_file = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in from_file))




if "__name__" == "__main__":
    unittest.main()
