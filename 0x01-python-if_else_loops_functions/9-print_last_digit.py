#!/usr/bin/python3


def print_last_digit(number):
    last_d = number % 10
    print("{:d}".format(last_d), end="")
    return last_d
