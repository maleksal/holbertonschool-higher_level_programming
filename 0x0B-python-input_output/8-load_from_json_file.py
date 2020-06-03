#!/usr/bin/python3
""" LoadFromJson Module """


def load_from_json_file(filename):
    ''' load from json file '''

    import json
    with open(filename, encoding='UTF8') as file:
        return json.loads(file)
