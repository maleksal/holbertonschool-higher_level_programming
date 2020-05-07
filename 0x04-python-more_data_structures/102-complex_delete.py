#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    l_keys = []
    for key, val in a_dictionary.items():
        if val == value:
            l_keys.append(key)

    for key in l_keys:
        del a_dictionary[key]

    return a_dictionary
