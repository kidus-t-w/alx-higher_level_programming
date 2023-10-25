#!/usr/bin/python3
"""Defines a function that creates an Object form a JSON file"""
import json


def load_from_json_file(filename):
    """"Creates an object form a JSON file
        Args:
            filename (str): file to be written in
    """
    with open(filename) as f:
        return json.load(f)
