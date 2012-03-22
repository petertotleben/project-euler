#!/usr/bin/python
#
# Project Euler -- Problem 37
# 
# Which primes are left and right truncatable and are prime at
# every stage (it is given that there are exactly 11 of these)


from math import ceil
from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n == 5:
        return True
    if n == 7:
        return True

    for i in range(2, int(ceil(sqrt(n)))+1):
        if (n % i) == 0:
            return False
    return True


def are_left_truncatables_prime(n):
    while (n != 0):
        if not is_prime(n):
            return False
        n /= 10
    return True


def are_right_truncatables_prime(n):
    power = 1
    while True:
        if not is_prime(n % (10**power)):
            return False
        if n == (n % (10**power)):
            break
        power += 1
    return True


if __name__ == "__main__":
    n = 11
    count = 0
    sum = 0
    while (count < 11):
        if (are_left_truncatables_prime(n)) and (are_right_truncatables_prime(n)):
            count += 1
            sum += n
            print "Here's one:  {0}".format(n)
        n+=1
    print "Answer is {0}".format(sum)
