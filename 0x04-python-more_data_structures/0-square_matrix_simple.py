#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    new = []
    for row in matrix:
        new_matrix = [x**2 for x in row]
        new.append(new_matrix)
    return new
