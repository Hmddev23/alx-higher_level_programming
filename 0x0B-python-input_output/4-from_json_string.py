#!/usr/bin/python3
"""define a function that return a python object"""
import json


def from_json_string(my_str):
    """convert JSON string into python object"""
    return json.loads(my_str)
