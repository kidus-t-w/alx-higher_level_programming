#!/usr/bin/python3
"""
Module: 2-matrix_divided.py
"""


def matrix_divided(matrix, div):
    """
        Divides all the elements of a matrix
        Args:
            matrix (list): list to be devided
            div (int): number to devide the list
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for column in matrix:
        new_row = []
        for j in column:
            new_row.append(round((j / div), 2))
        new_matrix.append(new_row)
    return new_matrix
