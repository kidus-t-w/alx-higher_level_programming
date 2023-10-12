#!/usr/bin/python3
"""
Module: 4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """
    Returns True if object is an instance of a class 
    Else returns False
    Args:
    obj (object): object to be checked
    a_class (class): class
    """
    if type(obj) == a_class:
        result = isinstance(a_class, obj)
        return result
    else:
        return False
