#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    """A program that adds all command line arguements"""

    len = len(sys.argv)
    sum = 0
    for i in range(1, len):
        sum = sum + int(sys.argv[i])
    print(f"{sum}")
