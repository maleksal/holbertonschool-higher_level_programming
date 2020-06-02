#!/usr/bin/python3
""" Rectangle module """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        self._width = self.integer_validator(None, width)
        self._height = self.integer_validator(None, height)
