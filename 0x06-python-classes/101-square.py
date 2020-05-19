#!/usr/bin/python3

'''Square module'''


class Square:
    '''
    Square class

    Atributes:
        __size (int): The size of a square is crucial for a square
        __position (int): Private instance attribute

    '''

    def __init__(self, size=0, position=(0, 0)):
        '''
        Constructor of the Square class

        Args:
            size (int): The size of square
            position (int): Private instance attribute

        '''

        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''
        Getter for position instance attribute

        '''
        return self.__position

    @position.setter
    def position(self, position):
        '''Instance attributes setter for position

        Args:
            position (tuple): tuple of 2 integer

        Return:
            TypeError: when not a tuple of 2 positive integers

        '''

        if type(position) != tuple or len(position) != 2\
                or type(position[0]) != int\
                or type(position[1]) != int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

        else:
            print("\n" * self.__position[1], end="")
            for i in range(0, self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    def __str__(self):
        '''
        represents a class, same behavior as my_print

        '''
        template = ""

        if self.__size == 0:
            return template

        else:
            template += '\n' * self.__position[1]

            for i in range(self.__size):
                template += ' ' * self.__position[0]
                template += "#" * self.__size
                if i < self.__size - 1:
                    template += "\n"
        return template
