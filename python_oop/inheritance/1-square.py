#!/usr/bin/env python3
"""Square module

Defines `Square` that inherits from `Rectangle`.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square shape where width == height == size."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size
