#!/usr/bin/puthon3
"""Reads a text file"""


def read_file(filename=""):
    """
    Reades a text file.
    Args:
        filename (str): file to be read
    """
    with open(filename, encoding="utf-8") as file_r:
        print(file_r.read())
