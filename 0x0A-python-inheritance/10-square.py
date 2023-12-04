#!/usr/bin/python3
"""
Module Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square class
    """
    def __init__(self, size):
        """
        initialize
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"
        are of square
        """
        return self.__size ** 2
