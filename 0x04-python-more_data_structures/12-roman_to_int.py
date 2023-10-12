#!/usr/bin/python3

def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or roman_string == ""):
        return 0

    ro_dictionary = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    number = 0

    for i in range(len(roman_string)):
        if ro_dictionary.get(roman_string[i], 0) == 0:
            return 0
        if (i != (len(roman_string) - 1)) and\
            ro_dictionary[roman_string[i]] < ro_dictionary[roman_string[i + 1]]:
            number += ro_dictionary[roman_string[i]] * -1
        else:
            number += ro_dictionary[roman_string[i]]
    return number
