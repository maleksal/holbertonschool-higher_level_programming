#!/usr/bin/python3
""" inhertis from class """


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and not type(obj) == a_class
