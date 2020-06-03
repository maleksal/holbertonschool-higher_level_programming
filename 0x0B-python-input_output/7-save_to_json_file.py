#!/usr/bin/python3
''' I/O & Json module '''


def save_to_json_file(my_obj, filename):
    '''  writes an Object to a text file, using a JSON representation '''

    import json

    # Serialize object
    serializer = json.dumps(my_obj)
    # write to file
    with open(filename, 'w+') as file:
        file.write(serializer)
