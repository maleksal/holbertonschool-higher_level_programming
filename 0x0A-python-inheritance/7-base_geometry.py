#!/usr/bin/python3
""" class module """


class BaseGeometry(object):
    """ BaseGeometry class """

    def area(self):
        ''' area method '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' validate int method '''
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
