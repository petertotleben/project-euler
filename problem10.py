#!/usr/bin/python
#
# Project Euler Problem 10
#
#
# This program finds the sum of all primes below 2,000,000

from math import ceil 
from math import sqrt

def is_prime(n):
    """This function returns true iff n is a prime number"""

    if n==2: 
      return True   # special case
    if (n%2) == 0:
      return False  # even numbers don't take much thought

    for i in range(3, int(ceil(sqrt(n))) + 1, 2):
        if (n%i) == 0: 
          return False

    return True





def sum_of_primes(n):
  """This function returns the sum of all primes less than n"""

  if n == 1:
    return 0
  if n == 2:
    return 2

  sum = 2
  for i in range(3, n):
    if is_prime(i):
      sum += i

  return sum



if __name__ == "__main__":
  print "The sum of primes less than 2,000,000 is {0}".format(sum_of_primes(2000000))
