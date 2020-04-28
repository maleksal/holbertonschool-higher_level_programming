#!/usr/bin/python3


def _convert(char, status):
    if status % 2 == 0:
        return chr(char)
    return chr(char).upper()


status = 0
for i in reversed(range(97, 123)):
    print("{}".format(_convert(i, status)), end="")
    status += 1
