#!/usr/bin/python
#
# Project Euler -- Problem 41
#
# What is the largest n-digit pandigital number

from math import ceil
from math import sqrt



def num_digits(n):
  num_digits = 0
  while n != 0:
    num_digits += 1
    n /= 10
  return num_digits



def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if (n % 2) == 0:
        return False

    for i in range(2, int(ceil(sqrt(n)))+1):
        if (n % i) == 0:
            return False
    return True


def is_pandigital(n):
  strnum = str(n)
  digit_list = [0] * 10
  for i in range(len(strnum)):
    digit_list[int(strnum[i])] = 1
  return reduce( (lambda x,y: x*y), digit_list[1:num_digits(n) +1])



if __name__ == "__main__":


  print "Checking 7 digit numbers . . ."
  for i in range(9999999, 999999, -1):
    if is_pandigital(i):
      if is_prime(i):
        print "The answer is {0}".format(i)

  print "Checking 4 digit numbers . . ."
  for i in range(9999, 999, -1):
    if is_pandigital(i):
      if is_prime(i):
        print "The answer is {0}".format(i)
