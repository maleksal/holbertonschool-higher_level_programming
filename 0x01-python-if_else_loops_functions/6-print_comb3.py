#!/usr/bin/python3


def check_digit(num):
    if num // 10 < num % 10:
        return True
    return False


for i in range(1, 99):

    if check_digit(i):
        if i != 89:
            print("{:02d}".format(i), end=", ")
        else:
            print(89)
