#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    len_argv = len(argv) - 1
    counter = 1
    text = "arguments"
    if len_argv == 0:
        print("{:d} arguments.".format(len_argv))
    else:
        if len_argv == 1:
            text = text[:-1]
        print("{:d} {}:".format(len_argv, text))
        for elem in argv[1:]:
            print("{:d}: {}".format(counter, elem))
            counter += 1
