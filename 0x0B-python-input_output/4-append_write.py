#!/usr/bin/python3
''' append to file Module '''


def append_write(filename="", text=""):
    ''' append to file '''

    with open(filename, 'a', encoding="UTF8") as file:
        file.write(text)
    return len(text)