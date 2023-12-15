#!/usr/bin/python3
"""Base Module"""
import json
import csv
import turtle
import random


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        toJson
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save to file
        """
        fileName = cls.__name__ + ".json"
        lis = []
        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                lis.append(list_objs[i].to_dictionary())
        output = cls.to_json_string(lis)

        with open(fileName, 'w') as f:
            f.write(output)

    @staticmethod
    def from_json_string(json_string):
        """
        from json to dict
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        return instance from dict
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                newObj = cls(1, 1)
            else:
                newObj = cls(1)
            newObj.update(**dictionary)
            return newObj

    @classmethod
    def load_from_file(cls):
        """
        load instance from file
        """
        fileName = str(cls.__name__) + ".json"
        try:
            with open(fileName, "r") as f:
                dictList = Base.from_json_string(f.read())
                result = []
                for item in range(len(dictList)):
                    result.append(cls.create(**dictList[item]))
                return result
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save csv file
        """
        fileName = cls.__name__ + ".csv"
        with open(fileName, "w", newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    instantList = ["id", "width", "height", "x", "y"]
                else:
                    instantList = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=instantList)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        load from csv
        """
        fileName = cls.__name__ + ".csv"
        try:
            with open(fileName, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    instantList = ["id", "width", "height", "x", "y"]
                else:
                    instantList = ["id", "size", "x", "y"]
                dictList = csv.DictReader(f, fieldnames=instantList)
                dictList = [dict([key, int(value)] for key, value in d.items())
                            for d in dictList]
                return [cls.create(**d) for d in dictList]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw
        """
        tortule = turtle.Turtle()
        tortule.title("draws")
        tortule.screen.bgcolor("#ffffff")
        turtle.hideturtle()
        tortule.color("purple")
        for r in list_rectangles:
            tortule.up()
            tortule.goto(r.x, r.y)
            tortule.down()
            for i in range(2):
                tortule.forward(r.width)
                tortule.left(90)
                tortule.forward(r.height)
                tortule.left(90)

        tortule.color("#red")
        for s in list_squares:
            tortule.up()
            tortule.goto(s.x, s.y)
            tortule.down()
            for i in range(2):
                tortule.forward(s.width)
                tortule.left(90)
                tortule.forward(s.height)
                tortule.left(90)
        turtle.exitonclick()
