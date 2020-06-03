#!/usr/bin/python3
"""write to fileModule """


def write_file(filename="", text=""):
    ''' write to file '''

    with open(filename, 'w+', encoding="UTF8") as file:
        file.write(text)
    return len(text)
