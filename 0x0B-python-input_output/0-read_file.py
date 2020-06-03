#!/usr/bin/python3
''' read file module '''

def read_file(filename=""):
    ''' read from file '''

    with open(filename, 'r', encoding='UTF8') as file:
        print(file.read())
