#!/usr/bin/python3
""" Read n lines module"""


def read_lines(filename="", nb_lines=0):
    ''' read n lines '''

    with open(filename, 'r') as file:
        lines = file.readlines()

    if nb_lines <= 0 or nb_lines >= len(lines):
        print("".join(lines), end='')
        return

    for i in range(nb_lines):
            print(lines[i], end='')
