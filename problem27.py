#!/usr/bin/python
#
# Project Euler, Problem 27
#
# Find the product of a and b where
# the polynomial n^2 + an + b produces the maximum number
# of consecutive primes for values of n (|a| and |b| < 1000)

from math import ceil
from math import sqrt

def eval_poly(a, b, n):
    return n*(n+a) + b



def is_prime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n == 4:
        return False

    for i in range(2, int(ceil(sqrt(n)))+1):
        if (n % i) == 0:
            return False
    return True



def prime_chain(a, b):
    n = 1
    while(is_prime(eval_poly(a, b, n))):
        n += 1 
    return n


def main():
    max_length = 0
    max_a = 0
    max_b = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            print "({0}, {1})".format(a, b)
            length = prime_chain(a, b)
            if length > max_length:
                max_a = a
                max_b = b
                max_length = length
    return max_a * max_b



if __name__ == "__main__":
    answer = main()
    print "The answer is {0}".format(answer)

