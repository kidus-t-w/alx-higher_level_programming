#!/usr/bin/python3
"""
Module: 1-rectangle.py
"""


class Rectangle:
    """
    Defines a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Defines height and width of the rectangle
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        pass

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an intiger")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        pass

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("widtth must be >= 0")
        else:
            self.__width = value
