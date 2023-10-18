#!/usr/bin/python3
"""Defines a square using Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square using Rectangle"""
    def __init__(self, size):
        if self.integer_validator("size", size):
            self.__size = size
            super().__init__(self.__size, self.__size)

    def __str__(self):
        return "[Square] " + str(self.__size)\
              + "/" + str(self.__size) + ""
