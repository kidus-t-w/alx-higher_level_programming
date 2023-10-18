#!/usr/bin/python3
"""
Module: 6-base_geometry.py
"""


class BaseGeometry:
    """
    BaseGeometry
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an intiger".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
