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
        """
        self.__size = size

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size
        Args:
            value (int): value of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """current square area
        Returns:
            current square area
        """
        return (self.__size) ** 2
