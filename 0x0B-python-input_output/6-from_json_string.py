#!/usr/bin/python3
''' Load Json Module '''


def from_json_string(my_str):
    ''' return from json string to data structure '''
    import json

    return json.loads(my_str)
