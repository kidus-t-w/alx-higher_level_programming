#!/usr/bin/python3
"""
Module: 6-base_geometry.py
"""


class BaseGeometry:
    """
    BaseGeometry
    """
    def area(self):
        """
        Not yet implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate a parameter as integer.
        Args:
            name (str): The name of the parameter
            value (int): The parameter to balidate
        Raises:
            TypeError: If value is not an integer.
            ValueError:If vavlue is <=
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))