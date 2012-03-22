#!/usr/bin/python
#
# Project Euler -- Problem 25
#
# Find the first Fibbonacci number to contain over 1000 digits

def has_thousand_digits(n):
  return n / (10**999)



def next_fib_number(n_minus_two, n_minus_one):
  return n_minus_two + n_minus_one



def find_number():
  n_minus_two = 1
  n_minus_one = 1
  n = 2
  term_number = 3
  while (not has_thousand_digits(n)):
    n_minus_two = n_minus_one
    n_minus_one = n
    n = next_fib_number(n_minus_two, n_minus_one)
    term_number += 1
  return term_number



if __name__ == "__main__":
    answer = find_number()
    print "The answer is {0}".format(answer)

