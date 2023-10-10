#!/usr/bin/python3
"""
Module: 3-is_kind_of_class.py
"""


def is_kind_of_class(obj, a_class):
    """
    The function returns True if the object is an instance of,
    or the object is an instance of a class that inherited from,
    the specified class; otherwise False.
    Args:
        obj (object): object to be checked
        a_class (class): class to be checked with
    """
    result = isinstance(obj, a_class)
    return result
