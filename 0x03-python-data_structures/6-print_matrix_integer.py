#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for j in range(0, len(item)):
            print("{:d}".format(item[j]), end="")
            if j != (len(item) - 1):
                print(" ", end="")
        print("")
