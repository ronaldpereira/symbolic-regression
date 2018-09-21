#!/usr/bin/python3

import math

def pow(x):
    if type(x) == int or type(x) == float:
        if x > 1 or x < 1:
            return x

    return 0

def sqrt(x):
    if type(x) == int or type(x) == float:
        if x > 0:
            return math.sqrt(x)

    return 0

def log(x):
    if type(x) == int or type(x) == float:
        if x > 0:
            return math.log(x)

    return math.log(0.00000000000000001)

def log2(x):
    if type(x) == int or type(x) == float:
        if x > 0:
            return math.log2(x)

    return math.log2(0.00000000000000001)

def log10(x):
    if type(x) == int or type(x) == float:
        if x > 0:
            return math.log10(x)

    return math.log10(0.00000000000000001)

def div(x):
    if type(x) == int or type(x) == float:
        if x != 0:
            return x

    return 0.00000000000000001


