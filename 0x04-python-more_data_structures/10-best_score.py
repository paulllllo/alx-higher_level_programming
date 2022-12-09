#!/usr/bin/python3

"""Function that returns the highest value in a dictionary"""


def best_score(a_dictionary):

    if a_dictionary:
        best_score = 0
        best = None
        for name in a_dictionary:
            if a_dictionary[name] > best_score:
                best_score = a_dictionary[name]
                best = name
        return best

    return None
