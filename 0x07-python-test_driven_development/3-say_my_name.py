#!/usr/bin/python3


def say_my_name(first_name, last_name=""):

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
