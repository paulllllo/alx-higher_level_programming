#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    """A program that does some stuff on 10 and 5"""

    len = len(sys.argv)
    if (len - 1) == 1:
        argn = 'argument'
    else:
        argn = 'arguments'
    if len > 1:
        dot = ':'
    else:
        dot = '.'
    print(f"{len - 1} {argn}{dot}")
    for i in range(1, len):
        print(f"{i}: {sys.argv[i]}")
