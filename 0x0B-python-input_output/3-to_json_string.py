#!/usr/bin/python3
"""
Defines a function which returns the json representaion
"""
import json


def to_json_string(my_obj):
    """
    Returns the json representaion
    Args:
        my_obj (any): object to be represented to json
    Returns:
        json representation
    """
    return json.dumps(my_obj)
