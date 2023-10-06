#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    lg_int = my_list[0]
    for i in range(len(my_list)):
        if lg_int < my_list[i]:
            lg_int = my_list[i]
    return lg_int
