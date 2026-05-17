#!/usr/bin/env python3
"""Shape abstractions and duck-typed shape info helper."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        radius = abs(self.radius)
        return math.pi * radius * radius

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
