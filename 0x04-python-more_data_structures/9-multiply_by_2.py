#!/usr/bin/python3

"""Function that multiplies each value in a dictionary by 2"""


def multiply_by_2(a_dictionary):

    new_dictionary = {i: (a_dictionary[i] * 2) for i in a_dictionary}
    return new_dictionary
