#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    def print_(x): print("{}: {}".format(x, a_dictionary.get(x)))
    [print_(x) for x in sorted(a_dictionary.keys())]
