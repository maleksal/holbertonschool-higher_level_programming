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
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ square size getter """
        return self.width

    @size.setter
    def size(self, value):
        ''' square size  setter '''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value <= 0:
            raise ValueError('size must be > 0')
        self.width = value
        self.height = value
