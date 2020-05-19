#!/usr/bin/python3

'''Square module'''


class Square:
    '''
    Square class

    Atributes:
        __size (int): The size of a square is crucial for a square

    '''

    def __init__(self, size=0):
        '''
        Constructor of the Square class

        Args:
            size (int): The size of square

        '''

        self.size = size

    @property
    def size(self):
        '''
        Instance attributes getter
        '''

        return self.__size

    @size.setter
    def size(self, size):
        '''Instance attributes setter

        Args:
            size(int): an int to be assigned to size

        Return:
            TypeError: when size is not an int
            ValueError: when size is less than 0

        '''

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        ''' Compute square area

        Return:
            integer: computed square area

        '''
        return self.__size ** 2

    def my_print(self):
        '''
        prints in stdout the square with the character #
        '''

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)
