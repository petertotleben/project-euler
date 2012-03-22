#!/usr/bin/python
#
# Project Euler Problem 23
#
# Find the sum of all positive integers that cannot be written as the sum of two abundant numbers

def divisor_sum(n):
  sum_divisors = 0
  for i in range(1, n):
    if n % i == 0:
      sum_divisors += i
  return sum_divisors



def get_abundant_numbers():
  print "Getting abundant numbers . . . "
  the_list = []
  for i in range(1, 28123):
    if (divisor_sum(i) > i):
      the_list.append(i)
  return the_list

def get_abundant_sums(abundant_number_list):
    print "Getting abundant sums . . . "
    sum_list = [0] * 28123 
    for i in range(len(abundant_number_list)):
        for j in range(i, len(abundant_number_list)):
            sum = abundant_number_list[i] + abundant_number_list[j]
            if sum < 28123:
                sum_list[sum] = 1
    return sum_list



def main():
  sum = 0
  sum_list = get_abundant_sums(get_abundant_numbers())
  print "summing . . . ."
  for i in range(1, 28123):
      if sum_list[i] == 0:
          sum += i
  return sum



if __name__ == "__main__":
  answer = main()
  print "The answer is {0}".format(answer)
