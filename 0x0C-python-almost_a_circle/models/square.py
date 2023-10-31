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
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """sets the value for height"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the arguments using *args and **kwargs"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                if a == 1:
                    self.size = arg
                if a == 2:
                    self.x = arg
                if a == 3:
                    self.y == arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
