#!/usr/bin/python3
"""
module testSquare
"""
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import io
import sys
import unittest


class TestSquare(unittest.TestCase):
    """TestSquare class"""

    def test_instance_of_base(self):
        self.assertIsInstance(Square(2), Base)

    def test_instance_of_rectangle(self):
        self.assertIsInstance(Square(2), Rectangle)

    def test_no_args_error(self):
        with self.assertRaises(TypeError):
            Square()

    def test_two_args_id_increment(self):
        square_a = Square(1, 2)
        square_b = Square(1, 2)
        self.assertEqual(square_a.id, square_b.id - 1)

    def test_size_private_error(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 2, 3, 4).__size)

    def test_size_getter(self):
        self.assertEqual(5, Square(1, 2, 3, 4).size)

    def test_size_setter(self):
        squa = Square(1, 2, 3, 4)
        squa.size = 12
        self.assertEqual(12, squa.size)

    def test_width_getter(self):
        squa = Square(1, 2, 3, 4)
        squa.size = 12
        self.assertEqual(12, squa.width)

    def test_height_getter(self):
        squa = Square(1, 2, 3, 4)
        squa.size = 1
        self.assertEqual(12, squa.height)

    def test_none_size_error(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_negative_size_error(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 10)

    def test_none_x_error(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, None)

    def test_negative_x_error(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -1, 0)

    def test_none_y_error(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)

    def test_negative_y_error(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -1)

    def test_area_small(self):
        self.assertEqual(4, Square(2, 0, 0, 1).area())

    def test_area_one_arg_error(self):
        squa = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            squa.area(1)

    def test_str_method_one_arg_error(self):
        squa = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            squa.__str__(1)

    def test_update_kwargs_one(self):
        squa = Square(10, 10, 10, 10)
        squa.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(squa))

    def test_to_dictionary(self):
        squaAA = Square(1, 2, 3)
        line = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(squaAA)
            self.assertEqual(str_out.getvalue(), line)
        self.assertEqual(squaAA.size, 1)
        self.assertEqual(squaAA.width, 1)
        self.assertEqual(squaAA.height, 1)
        self.assertEqual(squaAA.x, 2)
        self.assertEqual(squaAA.y, 3)
        self.assertEqual(squaAA.id, 1)
        line = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(squaAA.to_dictionary()))
            self.assertEqual(str_out.getvalue(), line)

    def test_value_square_error(self):
        with self.assertRaises(ValueError):
            squaAA = Square(-1)

    def test_load_from_file(self):
        squaAA = Square(5)
        squaB = Square(8, 2, 5)
        line = [squaAA, squaB]
        Square.save_to_file(line)
        loaded_output = Square.load_from_file()

        for i in range(len(line)):
            self.assertEqual(line[i].__str__(), loaded_output[i].__str__())