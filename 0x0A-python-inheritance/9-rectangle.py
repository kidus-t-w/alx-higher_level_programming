#!/usr/bin/python3
"""Defines a rectangle using BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry"""
    def __init__(self, width, height):
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def __str__(self):
        return "[Rectangle] " + str(self.__width)\
              + "/" + str(self.__height) + ""

    def area(self):
        return self.__height * self.__width
