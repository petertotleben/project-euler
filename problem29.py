#!/usr/bin/python
#
# Project Euler, Problem 29
#
# How many distinct terms are in {a^b: 2<=a<=100 ^ 2<=b<=100}

if __name__ == "__main__":
    the_list = []

    for a in range(2, 101):
        for b in range(2, 101):
            the_list.append(a**b)

    the_list = list(set(the_list))
    print "The answer is {0}".format(len(the_list))
