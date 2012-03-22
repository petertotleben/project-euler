#!/usr/bin/python
#
# Project Euler Problem 26
#
# Find d<1000 such that 1/d has the longest repeating cycle.
#
# Note that if d is prime, the period is the order of 10 mod p, ie the lowest k such that 
# 10^k mod p = 1

from math import ceil
from math import sqrt

def is_prime(n):
    for i in range(3, int(ceil(sqrt(n)))+1):
        if (n % i) == 0:
            return False
    return True

def order_of_ten(modulus):
    order = 1
    while ((10**order) % modulus) != 1:
        order += 1 
    return order

def main():
    max_d = 0
    max_order = 0
    for d in range(7, 1000, 2):
        print "d={0}".format(d)
        if is_prime(d):
            print "\td is prime"
            order = order_of_ten(d)
            print "\torder is {0}".format(order)
            if order > max_order:
                max_order = order
                max_d = d 
                print "\tnew max"
    return max_d


if __name__ == "__main__":
    answer = main()
    print "The answer is {0}".format(answer)

