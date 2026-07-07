#!/usr/bin/env python3
"""Rectangle module

Defines `Rectangle` that inherits from `BaseGeometry`.
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle shape with width and height."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of the rectangle."""
        return self.__width * self.__height
