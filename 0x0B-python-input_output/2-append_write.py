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
        f.write(text)
        char_num = 0
        for text_num in text:
            for c_num in text_num:
                char_num += 1
        return char_num
 