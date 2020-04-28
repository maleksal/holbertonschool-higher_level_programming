#!/usr/bin/python3


def fizzbuzz():
    for num in range(1, 100 + 1):

        result = ""
        if num % 3 == 0:
            result += "Fizz"
        if num % 5 == 0:
            result += "Buzz"
        elif result == "":
            result = num

        print("{}".format(result), end=" ")
