#!/usr/bin/python3
"""define a function that return the an object as JSON"""
import json


def to_json_string(my_obj):
    """convert python object into JSON file"""
    return json.dumps(my_obj)
