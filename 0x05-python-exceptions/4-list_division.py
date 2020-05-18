#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    temp_var = 0

    for i in range(list_length):
        try:
            temp_var = my_list_1[i] / my_list_2[i]
            new_list.append(temp_var)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        except(ValueError, TypeError):
            print("wrong type")
            new_list.append(0)

    return new_list
