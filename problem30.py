#!/usr/bin/python
#
# Project Euler -- Prublem # 30
#
# Find the sum of all numbers that can be written as the sum of the fifth powers of its digits
#
# The only trick here is to find an upper limit.  We're trying to find a number with digits d_i 
# such that
#      (d_n**5) + ... + (d_1**5) + (d_0**5) = (10**n)d_n + ... + 10d_1 + d_0
# an easy upper bound is to find an n so large that the LHS cannot possibly be larger than the 
# RHS.  Suppose all of the digits of our number were 9, then we would need to find an n so large
# that
#        9**5 + 9**5 + ... (for n+1 factors) < (10**n)*9 + ... * 10*9 + 9
#   ==>  (n+1)*(9**5) < 10**(n+1)
# or, equivalently, renumbering the digits from 1,
#         (9^5)*n < 10^n

def power_digit_sum(a, n):
    """Returns the sum of the nth powers of the digits of a"""
    sum = 0
    while (a != 0):
        sum += (a % 10) ** n
        a /= 10
    return sum

def find_upper_limit(n):
    """Return the upper limit for finding sums of nth powers of digits"""
    num_digits = 1
    while True:
        if (num_digits * (9**n)) < (10**num_digits):
            break
        num_digits += 1
    return 10**num_digits




if __name__ == "__main__":
    upper_limit = find_upper_limit(5)
    sum = 0
    for i in range(2, upper_limit):
        if power_digit_sum(i, 5) == i:
            print "{0}".format(i)
            sum += i
    print "The answer is {0}".format(sum)
