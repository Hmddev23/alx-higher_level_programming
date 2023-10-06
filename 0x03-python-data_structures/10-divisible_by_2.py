#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    tmp_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            tmp_list.append(True)
        elif my_list[i] % 2 == 1:
            tmp_list.append(False)
    return tmp_list
