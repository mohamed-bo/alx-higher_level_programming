#!/usr/bin/python3
"""
module MyInt
"""


class MyInt(int):
    """
    version of int class
    """

    def __eq__(self, other):
        """
        now is !=
        """
        return int(self) != other

    def __ne__(self, other):
        """
        no is ==
        """
        return int(self) == other
