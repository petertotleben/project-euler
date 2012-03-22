#!/usr/bin/python
#
# Project Euler -- Problem 35
#
# How many circular primes are there below 1,000,000

from math import ceil
from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    if n == 2: 
        return True

    for i in range(2, int(ceil(sqrt(n)))+1):
        if (n % i) == 0:
            return False

    return True

def rotate(n):
    if (n / 10) == 0:
        return n
    else:
        return int(str(n % 10) + str(n / 10))

def is_circular(n):
    n_rotated = rotate(n)
    while (n_rotated != n):
        if not is_prime(n_rotated):
            return False
        n_rotated = rotate(n_rotated)
    print "It is circular"
    return True



def num_circular_primes(max):
    num = 1 # count two already
    for i in range(3, max, 2):
        print "Working on {0}".format(i)
        if is_prime(i):
            if is_circular(i):
                num += 1
    return num


if __name__ == "__main__":
    answer = num_circular_primes(1000000)
    print "The answer is {0}"
