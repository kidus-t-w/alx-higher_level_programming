#!/usr/bin/python3
"""
Module: 2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """
    Returnes True if the object is exactly an instance
    of the specified class

    Args:
        obj (object): object to be checked
        a_class: class
    """

    is_instance = isinstance(obj, a_class)
    return is_instance
