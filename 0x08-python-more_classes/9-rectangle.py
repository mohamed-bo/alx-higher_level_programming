#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes Rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """string representation of the class"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([self.print_symbol *
                          self.__width for _ in range(self.__height)])

    def __repr__(self):
        """string representation of the rectangle .. by using eval()"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """called whene class deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """new Rectangle instance with width == height == size"""
        return cls(size, size)
