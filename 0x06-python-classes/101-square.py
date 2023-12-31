#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """square class
    Attributes:
        size (int): value of size of row
    """
    def __init__(self, size=0, position=(0, 0)):
        """constructer
        Args:
            size (int): value of size of row
        """
        self.size = size
        self.position = position

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
        if (type(value) is tuple and len(value) == 2) and \
            (type(value[0]) is int and type(value[1]) is int) and \
                (value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """override when str

        Returns:
            str: the string presentation of square
        """
        if self.__size == 0:
            return ''
        firstEmpty = '\n' * self.position[1]
        row = ' ' * self.position[0] + '#' * self.size
        square = '\n'.join(row for _ in range(self.size))
        square = firstEmpty + square
        return square
