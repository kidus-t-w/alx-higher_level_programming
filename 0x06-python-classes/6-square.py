#!/usr/bin/python3
"""Defines a squre"""


class Square:
    """This class defines a squre"""
    def __init__(self, size=0, positoin=(0, 0)):
        """Initialize a new squre.

        Args:
            size (int): The sie of the new square
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = positoin

    def area(self):
        """calculates the area of a squre"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to a give value

        Args:
            value (int): value which is going to set size
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for i in range(0, self.__size):
                    print('#', end="")
                print()

    @property
    def position(self):
        return (self.__position)
    
    @position.setter
    def position(self, value):
        if 