#!/usr/bin/python3
"""This is the base of all other classes"""


class Base:
    """Base for all the classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initilizing function
            Args:
                id (int): id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
