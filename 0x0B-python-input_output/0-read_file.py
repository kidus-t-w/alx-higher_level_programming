#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """
    Reades a text file.
    Args:
        filename (str): file to be read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
