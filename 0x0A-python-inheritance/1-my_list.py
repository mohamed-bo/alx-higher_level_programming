#!/usr/bin/python3
"""
My List module
"""


class MyList(list):
    """
    my list Class
    """
    def __init__(self):
        """
        initialize
        """
        super().__init__()

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
