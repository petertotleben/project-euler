#!/usr/bin/python
#
# Problem 53
#
# How many values of C(n,r) for 1<=n<=100 are greater than 1,000,000

from math import factorial


def C(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))


if __name__ == "__main__":
    answer = 0
    for n in range(23, 101):
        for r in range(1, n):
            if C(n, r) > 1000000:
                answer += 1
    print "The answer is {0}".format(answer)
