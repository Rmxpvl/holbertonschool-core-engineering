#!/usr/bin/env python3
def safe_print_division(a, b):
    result = None

    try:
        result = a / b

    except:
        pass

    finally:
        print("{} / {} = {}".format(result))

    return result
