#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    '''
    check if the object is an instance of,
    or if the object is an instance of a class that inherited from
    '''
    return isinstance(obj, a_class)
