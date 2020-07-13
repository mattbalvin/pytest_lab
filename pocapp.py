#!/usr/bin/env python

from libpoc.poc import simple_function


def use_simple_function():
    print(simple_function("foo"))
    return 0


rb = use_simple_function()
print("return: " + str(rb))
