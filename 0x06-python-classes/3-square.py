#!/usr/bin/python3
"""Defines a squre"""

class Squre:
    """Defines a square"""
    def __init__(self, size):
        """Initilizing a new squre

        Args:
            size (int): number to be squared
        """
        if isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns the square area"""
        return self.__size ** 2
