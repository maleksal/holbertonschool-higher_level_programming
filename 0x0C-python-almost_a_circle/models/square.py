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
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' updates class attributes '''
        property_names = ["id", "size", "x", "y"]
        if len(args) >= 1:
            for i in range(len(args)):
                setattr(self, property_names[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in property_names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """  returns the dictionary representation of a Rectangle """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
