#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    tmp_mat = []
    for x in matrix:
        tmp_mat.append(list(map(lambda x: x**2, x)))
    return (tmp_mat)
