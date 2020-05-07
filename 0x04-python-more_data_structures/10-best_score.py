#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary or a_dictionary is {}:
        return None
    return max(a_dictionary)
