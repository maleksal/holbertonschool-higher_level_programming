#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    len_argv = len(argv) - 1
    counter = 1
    if len_argv == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len_argv))
        for elem in range(1, len_argv + 1):
            print("{}: {}".format(counter, elem))
            counter += 1
