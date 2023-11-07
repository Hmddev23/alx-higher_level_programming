#!/usr/bin/python3
"""define a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """create an object from a json file"""
    with open(filename, "r") as fi:
        return json.load(fi)
