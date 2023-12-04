#!/usr/bin/python3
"""
Module BaseGeometry
"""


class BaseGeometry:
    """empty"""
    def area(self):
        """that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
