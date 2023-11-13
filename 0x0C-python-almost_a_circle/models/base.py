#!/usr/bin/python3
"""define the Base model class"""
from json import dumps, loads
import csv


class Base:
    """Base class model.

    representation of the "base" for all other classes in this project.

    private class Attributes:
        __nb_object (int): number of Base instances.
    """

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

    @staticmethod
    def from_json_string(json_string):
        """return the deserialization of a JSON string.

        Args:
            json_string (str): JSON string representation of a list of dictionaries.
        Returns:
            None or empty list.
        """
        if json_string is None or not json_string:
            return []
        return loads(json_string)
