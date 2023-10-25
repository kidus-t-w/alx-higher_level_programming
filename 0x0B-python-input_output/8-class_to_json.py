#!/usr/bin/python3
"""Defines a function that returns the dictionary discription 
with sample data structure for JSON Serialization object
"""


def class_to_json(obj):
    """Returns the dictionary discription
        Args:
            obj (any): is an instance of a Class
            return: dictionary
    """
    obj.__dict__
