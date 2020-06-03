#!/usr/bin/python3
''' I/O & Json module '''


def save_to_json_file(my_obj, filename):
    '''  writes an Object to a text file, using a JSON representation '''

    import json

    with open(filename, 'w+') as file:
        file.write(json.dumps(my_obj))
