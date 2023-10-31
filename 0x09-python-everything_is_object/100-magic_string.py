#!/usr/bin/python3
def magic_string():
    magic_str.n = getattr(magic_str, 'n', 0) + 1
    return ("BestSchool, " * (magic_str.n - 1) + "BestSchool")
