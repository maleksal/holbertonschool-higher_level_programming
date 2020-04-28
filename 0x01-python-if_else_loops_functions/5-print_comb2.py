#!/usr/bin/python3


def two_digit(num):
    if num <= 9:
        return 0
    return ""


def space(num):
    if num == 99:
        return "\n"
    return ", "


for i in range(100):
    print("{}{}{}".format(two_digit(i), i, space(i)), end="")
