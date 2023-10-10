#!/usr/bin/python3
"""The function returns the list of avaliable attributes and methods of an object"""


def lookup(obj):
    """Reterns the list of avaliable attributes

    Args:
        obj (object): object to be looked in to
    """
    list_obj = []
    list_obj = dir(obj)
    return list_obj
