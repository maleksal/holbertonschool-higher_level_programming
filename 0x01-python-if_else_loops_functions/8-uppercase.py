#!/usr/bin/python3


def uppercase(str):
    print("".join(chr(ord(i) - 32) for i in str))
