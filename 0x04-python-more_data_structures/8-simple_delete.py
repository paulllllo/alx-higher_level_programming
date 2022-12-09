#!/usr/bin/python3

"""Function that removes an element from a dictionary"""


def simple_delete(a_dictionary, key=""):

    if not key in a_dictionary:
        return a_dictionary
    del a_dictionary[key]
    return a_dictionary
