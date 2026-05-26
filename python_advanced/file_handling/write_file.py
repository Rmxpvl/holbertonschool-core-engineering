#!/usr/bin/env python3
"""Module for writing a string to a text file"""


def write_file(filename="", text=""):
    """write a UTF-8 string to a text file and return number of characters."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
