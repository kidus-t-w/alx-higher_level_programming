#!/usr/bin/python3
"""
Moduel: 0-add_integer.py
"""


def add_integer(a, b=98):
    """Returns the sum of two numbers
        Args:
        a (int): first number
        b (int): second number
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
