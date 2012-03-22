#!/usr/bin/python
#
# Project Euler #21 -- Find the sum of all amicable nubmers under 10000

def d(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors

def amicable_sum():
  sum = 0
  print "Divide by 0"
  print (3 / sum)
  for a in range(1, 10001):
    b = d(a)
    if (a != b) and (d(b) == a):
      sum += a
  return sum

if __name__ == "__main__":
  answer = amicable_sum()
  print "The answer is {0}".format(answer)
  print "Now let's divide by zero!"
  a = 3 / 0
  print "You should not see this."
