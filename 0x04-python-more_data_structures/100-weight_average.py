#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0

    s1 = sum(map(lambda x: x[0] * x[1], my_list))
    return s1 / sum([i[1] for i in my_list])
