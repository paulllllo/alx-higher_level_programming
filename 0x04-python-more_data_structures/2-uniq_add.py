#!/usr/bin/python3

"""Function that adds all the unique elemnts of a list"""


def uniq_add(my_list=[]):

    new_list = list(sorted(set(my_list)))
    sum = 0
    for i in new_list:
        sum = sum + i
    return sum
