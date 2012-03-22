#!/usr/bin/python
#
# Project Euler #45
#
# Find the number after 40755 which is triangular, hexagonal, and pentagonal.
from math import sqrt


def is_pent(p):
    n = (1 + sqrt(1 + 24*p)) / 6
    return n == int(n)

def hex(n):
    return n * (2*n - 1)

if __name__ == "__main__":
    n = 165
    while True:
        if is_pent(hex(n)):
            break
        n += 1
    print "The answer is {0}".format(hex(n))
