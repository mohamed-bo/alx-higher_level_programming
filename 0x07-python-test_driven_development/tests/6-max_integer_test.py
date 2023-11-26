#!/usr/bin/python3

"""
test max integer gunction
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    tsts functions
    """
    def test_positive_integers(self):
        """Test positive"""
        self.assertEqual(max_integer([1, 10, 3, 30]), 30)

    def test_negative_integers(self):
        """Test negative"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_pos_neg_integers(self):
        """Test mix"""
        self.assertEqual(max_integer([-9, 7, 3]), 7)

    def test_empty_list(self):
        """empty list"""
        self.assertIsNone(max_integer([]), None)

    def test_one_arg(self):
        """one integer"""
        self.assertEqual(max_integer([1]), 1)

    def test_none_argument(self):
        """Test None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_list_with_none(self):
        """Test list with difrent type"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 4, None])

    def test_integers_and_strings(self):
        """Test string"""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_dictionary(self):
        """Test dictionary"""
        with self.assertRaises(TypeError):
            max_integer([{'aa': 1}, {'aad': 2}])

    def test_characters_list(self):
        """Test characters"""
        self.assertEqual(max_integer(['a', 'c', 'd', 'v']), 'v')

    def test_numbers_character(self):
        """Test mix"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 's'])

    def test_float_numbers(self):
        """Test float"""
        self.assertEqual(max_integer([1.1, 2.2, 3.5, 3.9]), 3.9)


if __name__ == '__main__':
    unittest.main()
