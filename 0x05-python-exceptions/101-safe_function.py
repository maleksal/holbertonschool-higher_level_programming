#!/usr/bin/python3


def safe_function(fct, *args):
    from sys import stderr

    try:
        return fct(*args)
    except Exception as error:
        stderr.write("Exception: {}\n".format(str(error)))
        return None
