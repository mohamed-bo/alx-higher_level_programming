#!/usr/bin/python3
"""module test Base"""
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import unittest

class TestBase(unittest.TestCase):
    """test"""

    def test_default_id_increment(self):
        base_a = Base()
        base_b = Base()
        self.assertEqual(base_a.id, base_b.id - 1)

    def test_unique_id_assignment(self):
        self.assertEqual(9, Base(9).id)

    def test_nb_instances_after_unique_id(self):
        base_a = Base()
        base_b = Base(9)
        base_c = Base()
        self.assertEqual(base_a.id, base_c.id - 1)

    def test_modify_public_id(self):
        base_instance = Base(9)
        base_instance.id = 10
        self.assertEqual(10, base_instance.id)

    def test_private_nb_instances_attribute(self):
        with self.assertRaises(AttributeError):
            print(Base(9).__nb_instances)

    def test_str_id_assignment(self):
        self.assertEqual("hello", Base("hello").id)

    def test_two_args_error(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string_rectangle_type(self):
        rectangle_instance = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str, type(Base.to_json_string([rectangle_instance.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_with_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args_error(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_save_to_file_square(self):
        Square.save_to_file(None)
        lin = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), lin)
        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_with_none(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args_error(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_rectangle(self):
        Rectangle.save_to_file(None)
        lin = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), lin)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string_with_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_with_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args_error(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()