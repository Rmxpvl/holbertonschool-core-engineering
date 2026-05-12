#!/usr/bin/env python3

def safe_print_division(a, b):
    result = None

    try:
        result = a / b

    except:
        pass

    finally:
        print("Inside result: {}".format(result))

    print("{} / {} = {}".format(a, b, result))

    return result
