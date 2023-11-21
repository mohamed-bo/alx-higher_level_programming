#!/usr/bin/python3
"""task 10 Alx"""
import math


class MagicClass:
    """This class of task 10"""

    def __init__(self, radius=0):
        """Initializes the class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """The area of the circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate mohit circle"""
        return 2 * math.pi * self.__radius
