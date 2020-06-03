#!/usr/bin/python3

''' Student Class Module '''


class Student(object):
    ''' Student Class '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return Student.__dict__
