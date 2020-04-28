#!/usr/bin/python3


def print_last_digit(number):
    last_d = number % 10
    if number < 0:
        last_d *= -1
    print("{:d}".format(last_d), end="")
    return last_d
