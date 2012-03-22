#!/usr/bin/python
#
# Project Euler Problem 15
#
# Number of Routes Through a Grid


def num_routes(i, j, size):
  if (i == size) or (j == size):
    return 1
  else:
    return num_routes(i+1, j, size) + num_routes(i, j+1, size)

if __name__ == "__main__":
  answer = num_routes(0, 0, 20)
  print "The answer is {0}".format(answer)
