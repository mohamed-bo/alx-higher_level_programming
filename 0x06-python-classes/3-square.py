#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """square class
    Attributes:
        size (int): value of size of line
    """
    def __init__(self, size=0):
        """constructer
        Args:
            size (int): value of size of line
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """current square area
        Returns:
            current square area
        """
        return (self.__size) ** 2
