#!/usr/bin/python3


def check_digit(num):

    def convert(number):
        return "{:02d}".format(number)

    if int(convert(num)) > int(convert(num)[::-1]):
        return False
    return True


for i in range(1, 99):

    if check_digit(i):
        if i != 89:
            print("{:02d}".format(i), end=", ")

        else:
            print(89)
