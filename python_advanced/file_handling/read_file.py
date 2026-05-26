#!/usr/bin/env python3
"""Module for reading a text file and printing it to stdout."""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
