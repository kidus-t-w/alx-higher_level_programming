#!/usr/bin/puthon3
"""Reads a text file"""


def read_file(filename=""):
    """
    Reades a text file.
    Args:
        filename (str): file to be read
    """
    with open(filename, encoding="UTF8") as file_r:
        file_r.read()
