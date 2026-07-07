#!/usr/bin/env python3
"""BaseGeometry module

Defines the BaseGeometry class with basic validation and an abstract
area method to be implemented by subclasses.
"""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an exception signalling area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that "value" is a positive integer.

        Args:
            name (str): parameter name used in error messages
            value: value to validate

        Raises:
            TypeError: if value is not an int
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
