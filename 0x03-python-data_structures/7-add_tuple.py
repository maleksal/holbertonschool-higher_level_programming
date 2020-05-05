#!/usr/bin/python3


def correct_tuple(tupl):
    len_t = len(tupl)
    tt = ()
    if len_t < 2:
        for i in range(2 - len_t):
            tt += (0,)

    return tt


def add_tuple(tuple_a=(), tuple_b=()):
    t = ()

    tuple_a += correct_tuple(tuple_a)
    tuple_b += correct_tuple(tuple_b)

    for i in range(len(tuple_a)):
        t += (tuple_a[i] + tuple_b[i],)

    return t
