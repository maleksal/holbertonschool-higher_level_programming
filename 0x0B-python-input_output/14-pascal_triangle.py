#!/usr/bin/python3
''' pascal triangle Module '''


def pascal_calculation(my_list):
    ''' calculate numbers inside list '''
    new = []
    prevElement = 0
    counter = 0

    for i in my_list:
        new.append(i + prevElement)
        prevElement = i
        counter += 1

    # append last element
    new.append(my_list[-1])

    return new


def pascal_triangle(n):
    ''' returns a list of lists of integers representing Pascal’s triangle '''
    matrix = [[1]]

    for i in range(n - 1):
        new_list = pascal_calculation(matrix[-1])
        matrix.append(new_list)
    return matrix
