#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Returns the number of characters writtern
        Args:
            filename (str): File to be written on
            text (str): String to be written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        char_num = 0
        for letters in text:
            for c_num in letters:
                char_num += 1
        return char_num
