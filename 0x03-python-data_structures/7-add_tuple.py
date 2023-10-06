#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tmp_1 = tuple_a + (0, 0)
    tmp_2 = tuple_b + (0, 0)
    return (tmp_1[0] + tmp_2[0], tmp_1[1] + tmp_2[1])
