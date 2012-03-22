#!/usr/bin/python
#
# Project Euler, Problem 55
#
# How many Lychrel numbers are there below 10000

def reverse(strnum):
  if len(strnum) == 1:
    return strnum
  else:
    return reverse(strnum[1:]) + strnum[0]


def is_palindrome(strnum):
    if len(strnum) == 0:
        return True
    elif len(strnum) == 1:
        return True
    else:
        if (strnum[0] == strnum[-1]) and is_palindrome(strnum[1:-1]):
            return True
        else:
            return False



if __name__ == "__main__":
  how_many = 0
  for n in range(10000):
    cur = n
    is_lychtel = True
    for i in range(50):
      cur += int(reverse(str(cur)))
      if is_palindrome(str(cur)):
        is_lychtel = False
        break
      else:
    if is_lychtel:
      how_many += 1
  print "The answer is {0}".format(how_many)

