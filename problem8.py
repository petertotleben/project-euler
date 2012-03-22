#!/usr/bin/python
#
# Project Euler Problem 8
#
# The problem is to find the largest product of five consecutive digits in the 1,000 digit number
# storded in problem8.dat


def get_number(filename):
  """Returns a string containing the digits of the number in the data file"""

   try:
    handle = open(filename, "r")
    lines = handle.readlines()
  except IOError as (errno, strerr):
    print "There was an error reading {0}:  {1}".format(filename, strerr)
  finally:
    handle.close()

 return reduce ( (lambda m, n: "".join((m.strip(), n.strip()))), lines )


  find_max_product(filename, chain_length):
  """Gets a number from filename and returns the maximum product of "chain_length" consecutive digits"""
  
  number = get_number(filename)

  max_product = 0
  for i in range(0, len(number) - chain_length + 1):
    product = 1
    for j in range(i, i + chain_length):
      product *= int(number[j])
    if product > max_product:
      max_product = product

  return max_product



if __name__ == "__main__":
  max_product = find_max_product("problem8.dat", 5)
  print "The maximum product is: {0}".format(max_product)



