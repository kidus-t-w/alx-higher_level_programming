#!/usr/bin/python3
"""Defines a function which appends a string to a file"""


def append_write(filename="", text=""):
    """
        Returns the number of characters.
        Args:
            filename (str): File to be appended on.
            text (str): String to be appended.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
