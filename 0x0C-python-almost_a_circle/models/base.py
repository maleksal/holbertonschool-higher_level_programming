#!/usr/bin/python3
''' Base Module '''
import json


class Base(object):
    ''' Base Class'''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w+') as file:
            if list_objs is None:
                file.write('[]')
            else:
                new = []
                for item in list_objs:
                    new.append(item.to_dictionary())
                file.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """  returns the list of the JSON string representation json_string """
        if json_string is None:
            return []
        return json.loads(json_string)
