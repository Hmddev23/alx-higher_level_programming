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
