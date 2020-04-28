#!/usr/bin/python3


def uppercase(str):
    def convert(c):
        if 97 <= ord(c) <= 122:
            return chr(ord(c) - 32)
        return c

    for i in str:
            print("{}".format(convert(i)), end="")
    print()
