#!/usr/bin/python3
"""Defines a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initilizes attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overides __str__ method"""
        return ("[Square] ({}) {}/{} - <size>"
                .format(self.id, self.x, self.y, self.width))
