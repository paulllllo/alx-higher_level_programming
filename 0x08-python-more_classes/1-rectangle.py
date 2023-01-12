#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """A class that contains some attributes and methods/
    around a rectange"""
    def __init__(self, width=0, height=0):
        """A rectangle with width and height attributes"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not (isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if not (isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
