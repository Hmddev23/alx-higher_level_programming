#!/usr/bin/python3
"""define the Base model class"""
from json import dumps, loads
import csv


class Base:
    """representation of the Base for all other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of a new Base.

        Args:
            id (int): Base class id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the serialization JSON of a dicts list.

        Args:
            list_dictionaries (list): List of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the serialization JSON of a list of objects to a file.

        Args:
            list_objs (list): List of Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """return the deserialization of a JSON string."""
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new
