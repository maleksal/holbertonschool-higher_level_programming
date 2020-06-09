#!/usr/bin/python3
''' Rectangle Module '''

from models.base import Base


class Rectangle(Base):
    ''' Rectangle class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' class constructor '''
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' getter for width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        ''' getter for height '''
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        ''' getter for x '''
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        ''' getter for y '''
        return self.__y

    @y.setter
    def y(self, value):
        """ y getter """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        ''' calculates area '''
        return self.__width * self.__height

    def display(self):
        ''' displays # on stdout '''
        if self.__y != 0:
            print('\n' * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        ''' updates class attributes '''
        property_names = ["id", "width", "height", "x", "y"]
        if len(args) >= 1:
            for i in range(len(args)):
                setattr(self, property_names[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        ''' represents class '''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
