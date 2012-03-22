#!/usr/bin/python
#
# Project Euler Problem 309
#
# Integer Solutions of the Crossing Ladder Problem

from math import sqrt

def is_soln(x, y, h, w):
  return (( 1 / sqrt(x**2 - w**2) ) + ( 1 / sqrt(y**2 - w**2) )) == (1/h) 



if __name__ == "__main__":
  count = 0

  print "Here we go!"
  for x in range(1, 1000000):
    print "x={0}".format(x)
    for y in range(x, 1000000):
      for h in range(1, x):
        for w in range(1, x):
          if is_soln(float(x), float(y), float(h), float(w)):
            print "Found a soln: ({0}, {1}, {2}, {3})".format(x, y, h, w)
            count += 1

  print "The answer is {0}".format(count)


