#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for e in i:
            print("{:d}".format(e), end="")
            if i[-1] != e:
                print(end=" ")
        print()
