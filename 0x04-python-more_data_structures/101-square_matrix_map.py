#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda x: x*x, x)) for x in matrix]
