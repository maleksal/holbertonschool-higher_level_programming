#!/usr/bin/python3


def remove_char_at(str, n):
    output = list(str)

    if n < len(str) and n >= 0:
        output.pop(n)
    return "".join(output)
