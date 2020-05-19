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

        self.__set(size)

    def __get(self):
        '''
        Instance attributes getter
        '''

        return self.__size

    def __set(self, size):
        '''Instance attributes setter

        Args:
            size(int): an int to be assigned to size

        Return:
            TypeError: when size is not an int
            ValueError: when size is less than 0

        '''

        if type(size) != int:
            raise TypeError("size must be an intege")

        if size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size
