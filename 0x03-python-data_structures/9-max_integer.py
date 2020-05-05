#!/usr/bin/python3


def max_integer(my_list=[]):
    max_n = 0

    if not my_list:
        return None

    for i in my_list:
        if i > max_n:
            max_n = i
    return max_n
