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

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == 'Rectangle':
            temporary = cls(1, 1)
        else:
            temporary = cls(1)
        temporary.update(**dictionary)
        return temporary

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        import os

        filename = "{}.json".format(cls.__name__)
        main_list = []

        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            lists = cls.from_json_string(file.read())
        for i in lists:
            main_list.append(cls.create(**i))
        return main_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        ''' draw rectongle and square using turtle '''
        import turtle

        def draw_square(size):
            t = turtle.Turtle()
            t.forward(size)
            t.left(90)
            t.forward(size)
            t.left(90)
            t.forward(size)
            t.left(90)
            t.forward(size)
            t.left(90)

        def draw_rectangle(width, height):
            t = turtle.Turtle()
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)

        for i in list_rectangles:
            draw_rectangle(i.width, i.height)
        for i in list_squares:
            draw_square(i.size)
