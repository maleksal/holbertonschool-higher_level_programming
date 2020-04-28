#!/usr/bin/python3
import random


def conditions(last_digit):
    result = ""

    if last_digit < 6 and last_digit != 0:
        result += "and is less than 6 and not 0"

    elif last_digit == 0:
        result += "and is 0"

    else:
        result += "and is greater than 5"

    return result


def last_digit(num):
    last_d = int(str(number)[-1])

    if num < 0:
        return -last_d
    return last_d


number = random.randint(-10000, 10000)

last_d = last_digit(number)
output = conditions(last_d)

print("Last digit of {} is {} {}".format(number, last_d, output))
