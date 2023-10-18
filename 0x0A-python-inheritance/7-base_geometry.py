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
            raise TypeError("<name> must be an intiger")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
