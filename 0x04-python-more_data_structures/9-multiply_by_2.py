#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    temporary_dictionary = a_dictionary.copy()
    for i in temporary_dictionary.keys():
        temporary_dictionary[i] *= 2
    return temporary_dictionary
