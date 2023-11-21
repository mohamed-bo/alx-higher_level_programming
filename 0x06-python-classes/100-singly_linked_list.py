#!/usr/bin/python3
"""Module of singly linked list"""


class Node():
    """
    Class of item in singly linked list
    """

    def __init__(self, data, next_node=None):
        """initialize attribute of node

        Args:
            data (int): value
            next_node (Node): next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter of data"""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """getter of next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of next node"""
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """Class a singly linked list"""

    def __init__(self):
        """Initialize list
        Args:
        data (int): value
        next_node (Node): next Node
        """
        self.__head = None

    def __str__(self):
        """overrid str functction of class"""
        str_rep = ""
        itr = self.__head
        if itr is not None:
            while itr is not None:
                str_rep += str(itr.data) + '\n'
                itr = itr.next_node
        return str_rep[:-1]

    def sorted_insert(self, value):
        itr = self.__head
        if itr is None or itr.data >= value:
            self.__head = Node(value, itr)
        else:
            while itr.next_node is not None and itr.next_node.data < value:
                itr = itr.next_node
            itr.next_node = Node(value, itr.next_node)


if "__main__" == __name__:
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
