#!/usr/bin/python
#
# Project Euler Problem 28
# 
# The sum of the diagonals on a 1001 x 1001 spiral

def spiral_sum(n):
    """ n had better be odd! """
    if n == 1:
        return 1
    else:
        return spiral_sum(n-2) + 4*n*n - 6*n + 6

if __name__ == "__main__":
    answer = spiral_sum(1001)
    print "The answer is {0}".format(answer)
    
