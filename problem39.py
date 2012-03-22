#!/usr/bin/python
#
# Project Euler Problem 39
#
# For which number <= 1000 are there the most pythagorean triples?

if __name__ == "__main__":
    max_solns = 0
    max_p = 0
    for p in range(16, 1001):
        solns = 0
        for a in range(1, p+1):
            for b in range(a, p+1):
                c = p - a - b
                if c > 0:
                    if (a**2 + b**2) == (c**2):
                        solns+=1
        if solns > max_solns:
            max_solns = solns
            max_p = p

    print "The answer is {0}".format(max_p)

