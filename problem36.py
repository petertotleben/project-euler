#!/usr/bin/python
#
# Project Euler Problem 36
#
# Find the sum of all numbers less than 1,000,000 whose decimal and binary representations are both
# palindromes


def is_palindrome(a_string):
    if len(a_string) == 0:
        return True
    elif len(a_string) == 1:
        return True
    else:
        if (a_string[0] == a_string[-1]) and is_palindrome(a_string[1:-1]):
            return True
        else:
            return False

def max_power_two(decimal_num):
    power = 0
    while 2**power <= decimal_num:
        power += 1
    return power - 1


def binary_string(decimal_num):
    str = ''
    max_power = max_power_two(decimal_num)
    for n in range(max_power, -1, -1):
        value = 2**n
        if value <= decimal_num:
            str += '1'
            decimal_num -= value
        else:
            str += '0'
    return str



def both_are_palindromes(decimal_num):
    if is_palindrome(str(decimal_num)) and is_palindrome(binary_string(decimal_num)):
        return True
    else:
        return False


def sum_of_palindromes(max):
    sum = 0
    for i in range(max):
        if both_are_palindromes(i):
            sum += i
    return sum



if __name__ == "__main__":
    answer = sum_of_palindromes(1000000)
    print "The answer is {0}".format(answer)


