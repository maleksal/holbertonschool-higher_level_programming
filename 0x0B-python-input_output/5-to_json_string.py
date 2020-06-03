#!/usr/bin/python3

''' Json Module '''


def to_json_string(my_obj):
    ''' returns the JSON representation of an object '''
    import json

    return json.dumps(my_obj)
