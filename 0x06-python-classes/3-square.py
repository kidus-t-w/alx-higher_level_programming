#!/usr/bin/python3
"""Defines a squre"""


class Square:
    """This class defines a squre"""
    def __init__(self, size=0):
        """Initialize a new squre.

        Args:
            size (int): The sie of the new square
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the square area"""
        return self.__size ** 2
