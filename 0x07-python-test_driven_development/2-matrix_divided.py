#!/usr/bin/python3


def matrix_divided(matrix, div):

    tracklistsize = len(matrix[0])
    new_matrix = []

    if not type(div) in [int, float]:
        raise TypeError("div must be a number")

    elif div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        if type(i) is not list:
            raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

        lengthlist = len(i)
        if tracklistsize != lengthlist:
            raise TypeError("Each row of the matrix must have the same size")

        for elem in i:
            if type(elem) not in [int, float]:
                raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        # new matrix list
        new_matrix.append([round(x/div, 2) for x in i])

        tracklistsize = lengthlist
    return new_matrix
