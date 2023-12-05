#!/usr/bin/python3
"""
Module student
"""


class Student:
    """
    student Class
    """

    def __init__(self, first_name, last_name, age):
        """
        class initialization
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        class to json
        """

        if attrs is not None:
            di = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    di[key] = value
            return di
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        reload from json
        """

        for key, value in json.items():
            setattr(self, key, value)
