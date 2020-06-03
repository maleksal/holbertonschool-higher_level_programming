#!/usr/bin/python3
''' get number of lines module '''


def number_of_lines(filename=""):
    ''' get number of lines '''

    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)
