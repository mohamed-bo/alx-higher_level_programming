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
        if type(value) is not int and type(value) is not float:
            raise TypeError("size must be a number")
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

    def __eq__(self, other):
        """
        overrid equality operator
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        overrid inequality operator
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        overrid greater than operator
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        overrid greater than or equal
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        overrid less than
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        overrid less than or equal
        """
        return self.area() <= other.area()
