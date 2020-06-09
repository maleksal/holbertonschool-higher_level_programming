#!/usr/bin/python3
''' Square Module '''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' class constructor '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            id, self.__x, self.__y, self.__width)
