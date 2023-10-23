#!/usr/bin/python3
"""
Defines a function which returns an object represented by JSON
"""
import json


def from_json_string(my_str):
    """
    Defines a function which returns an object represented by JSON
    Args:
        my_str (any): object to be represented
    """
    return json.loads(my_str)
