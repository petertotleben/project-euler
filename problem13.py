#!/usr/bin/python 
#
# Project Euler Problem 13
# 
# Find the first 10 digits in the sum of the numbers in problem13.dat

def main(filename):

  try:
    handle = open(filename, "r")
    lines = handle.readlines()
  except IOError as (errno, strerr):
    print "There was an error reading {0}:  {1}".format(filename, strerr)
  finally:
    handle.close()

  lines = [int(line.strip()) for line in lines]
  sum = reduce( (lambda x, y: x+y), lines )
  return str(sum)[0:10]

if __name__ == "__main__":
  answer = main("problem13.dat")
  print "The answer is {0}".format(answer)
  


