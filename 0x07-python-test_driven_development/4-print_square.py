#!/usr/bin/python3


def print_square(size):
    """
    print square with character #

    Args:
        size(int): the size length of the square

    Returns:
        TypeError:
                if size is not an int
                if size is float and less than 0
        ValueError: if size is less than 0

    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
