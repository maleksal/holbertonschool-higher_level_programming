#!/usr/bin/python3


def safe_print_division(a, b):
    temp_var = 0
    try:
        temp_var = a / b
    except:
        return None
    finally:
        print("Inside result: {}".format(temp_var))
    return temp_var
