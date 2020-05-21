#!/usr/bin/python3

"""
Add integer module
functions:
    add_integers
"""


def add_integer(a, b=98):
    """ add two integers
    return a + b
    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")

    if not type(b) in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
