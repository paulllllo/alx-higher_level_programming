#!/usr/bin/python3

"""Function to square all the integers in a matrix"""

def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda item: [i**2 for i in item], matrix))
    return new_matrix
