#!/usr/bin/env python3
"""Square with customized string representation

Prints as [Square] <size>/<size>
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square where width == height == size."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
