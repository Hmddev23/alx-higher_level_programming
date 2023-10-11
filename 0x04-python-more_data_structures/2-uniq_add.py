#!/usr/bin/python3

def uniq_add(my_list=[]):
    n_list = []
    total = 0
    for number in my_list:
        if number not in n_list:
            total += number
            n_list.append(number)
    return total
