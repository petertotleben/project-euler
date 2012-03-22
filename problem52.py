#!/usr/bin/python
#
# Project Euler Problem 52
#
# Find the smallest postive integer n such that n, 2n, 3n, 4n, 5n, and 6n contain the same digits.

def make_digit_list(n):
    digit_list = [0] * 10

    nstring = str(n)
    for i in range(len(nstring)):
        digit_list[int(nstring[i])] = 1

    return digit_list



def are_lists_equal(list1, list2):
    for i in range(10):
        if list1[i] != list2[i]:
            return False
    return True



def main():
    n = 2
    while True:
        digit_list = make_digit_list(n)
        lists_equal = True
        for i in range(2, 7):
           if not are_lists_equal(digit_list, make_digit_list(n*i)):
               lists_equal = False
               break
        if lists_equal:
            break
        else:
            n += 1
            continue
    return n



if __name__ == "__main__":
    answer = main()
    print "The answer is {0}".format(answer)


