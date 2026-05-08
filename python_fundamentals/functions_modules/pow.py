#!/usr/bin/env python3

def pow(a, b):
    result = 1

    if b < 0:
        for i in range(-b):
            result = result * a
        return 1 / result

    for i in range(b):
        result = result * a

    return result
