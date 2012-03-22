#!/usr/bin/python
#
# Project Euler Problem 56
# 
# What number a**b for a, b < 100 has the maximal digital sum

def digit_sum(n):
  sum = 0
  while n != 0:
    sum += (n%10)
    n /= 10
  return sum



if __name__ == "__main__":
  max_sum = 0
  for a in range (100):
    for b in range (100):
      sum = digit_sum(a**b)
      if sum > max_sum:
        max_sum = sum
  print "The answer is {0}".format(max_sum)
