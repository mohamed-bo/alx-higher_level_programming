#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """square class
    Attributes:
        size (int): value of size of line
    """
    def __init__(self, size=0, position=(0, 0)):
        """constructer
        Args:
            size (int): value of size of line
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter of size
        Returns:
            The value of size
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

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """getter of size"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of position
        Args:
            value (tuple): position in the square.
        """
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
