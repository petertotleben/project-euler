#!/usr/bin/python
#
# Project Euler -- Problem 34
#
# Find the sum of all numbers such that the sum of the factorials of the number's digits is equal to
# the number itself (eg. 1! + 4! + 5! = 145)
#
# The argument for establishing the upper bound is similar to the one for problem 30

from math import factorial


def fact_of_digit(n):
    sum = 0
    while n != 0:
        sum += factorial((n % 10))
        n /= 10
    return sum



def find_upper_bound():
    n = 2
    while True:
        if (n * factorial(9)) < (10**n):
            break
        n += 1
    return 10**n


def main():
    print "Finding upper bound . . . "
    upper_bound = find_upper_bound()
    print "Done! Upper bound is {0}".format(upper_bound)
    sum = 0
    for i in range(3, upper_bound):
        if i == fact_of_digit(i):
            print "{0}".format(i)
            sum += i
    return sum



if __name__ == "__main__":
    answer = main()
    print "The answer is {0}".format(answer)

