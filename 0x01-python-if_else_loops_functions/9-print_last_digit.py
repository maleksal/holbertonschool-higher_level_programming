#!/usr/bin/python3


def print_last_digit(number):
    last_d = int(str(number)[-1])
    if number < 0:
        last_d *= -1
    print(last_d, end="")
    return last_d
