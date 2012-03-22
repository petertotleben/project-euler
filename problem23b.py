#!/usr/bin/python
#
# Project Euler Problem 23, attempt 2
# 
# Find all the numbers that cannot be written as the sum of two abundant numbers

def is_abundant(n):
    if proper_divisor_sum(n) > n:
        return True
    else:
        return False



def proper_divisor_sum(n):
    sum = 1
    for i in range(2, n):
        if n % i == 0:
            sum += i
    return sum



def is_sum_of_abundants(n, abundant_list):
    for i in range(len(abundant_list)):
        if abundant_list[i] > n:
            break
        for j in abundant_list[i:]:
            if abundant_list[i] + j == n:
                return True
    return False


def main():
    abundant_list = []
    sum = (23*24) / 2 # 1 to 23 can be written as the sum of two abundant numbers
    for i in range(24, 28123):
        print "i={0}".format(i)
        if is_abundant(i):
            abundant_list.append(i)
        if not is_sum_of_abundants(i, abundant_list):
            sum += i
    return sum



if __name__ == "__main__":
    answer = main()
    print "The answer is {0}".format(answer)

