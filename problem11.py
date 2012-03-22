#!/usr/bin/python
#
# Project Euler Problem 12
# 
# Find the largest product of consecutive entries in the matrix stored in problem11.dat

def load_matrix(filename):
  """Loads the matrix stored in "filename" and return it as a row-wise list of lists.  It is assumed
  that the elements of a row are separated by a space and the rows themselves are separated by a
  newline."""

  try:
    handle = open(filename, "r")
    rows = handle.readlines()
  except IOError as (errno, strerr):
    print "There was an error reading {0}:  {1}".format(filename, strerr)
  finally:
    handle.close()

  return [row.split() for row in rows]



def max_row_product(matrix, length):
  """ Finds the maximum product in the rows of "matrix" with length "length" """

  max_product=0;
  for i in range(len(matrix)):
    for j in range(len(matrix[i]) - length + 1):
      current_product = 1
      for k in range(length):
        current_product *= int(matrix[i][j+k])
      if current_product > max_product:  max_product = current_product
  return max_product



def find_lr_product(matrix, i, j, length):
  """ Returns the product of "length" entries along the left-right diagonal of "matrix" beginning at
  position (i,j).  It returns None if there are not enough entries along the diagonal for this to be
  possible """

  print "start: ({0}, {1})".format(i, j)

  num_factors = 0
  current_product = 1
  while (i < len(matrix)) and (j < len(matrix[i])) and (num_factors < length):
    current_product *= int(matrix[i][j])
    num_factors += 1
    i += 1
    j += 1

  print "end:  ({0}, {1})".format(i, j)

  if num_factors == length:
    return current_product
  else:
    return None


def upper_triangular_l_to_r(matrix, length):
  """ Finds the maximum product along the diagonals of the upper triangle of the matrix, oriented
  from left to right """

  max_product = 0
  j = 0
  while (j < len(matrix[0])):
     i = 0
     jtemp = j
     while (i < len(matrix)) and (jtemp < len(matrix[i])):
       product = find_lr_product(matrix, i, jtemp, length)
       if (product != None) and (product > max_product):
         max_product = product
       i += 1
       jtemp += 1
     j += 1
  return max_product



def find_rl_product(matrix, i, j, length):
  num_factors = 0
  current_product = 1
  while (i < len(matrix)) and (j >= 0) and (num_factors < length):
    current_product *= int(matrix[i][j])
    num_factors += 1
    i += 1
    j -= 1
  if num_factors == length:
    return current_product
  else:
    return None



def upper_triangular_r_to_l(matrix, length):
  max_product = 0
  j = 0
  while (j < len(matrix[0])):
    i = 0
    jtemp = j
    while (i < len(matrix)) and (jtemp >= 0):
      product = find_rl_product(matrix, i, jtemp, length)
      if (product != None) and (product > max_product):
        max_product = product
      i += 1
      jtemp -= 1
    j += 1
  return max_product
    

def max_diag_product(matrix, length):
  """ Finds the maximum product in the diagonals of "matrix" with length "length" """

  product1 = upper_triangular_l_to_r(matrix, length)
  product2 = upper_triangular_l_to_r(zip(*matrix), length)
  product3 = upper_triangular_r_to_l(matrix, length)
  product4 = upper_triangular_r_to_l(zip(*matrix), length)

  print "(1, 2, 3, 4) = ({0}, {1}, {2}, {3})".format(product1, product2, product3, product4)
  return max([product1, product2, product3, product4]) 


def find_max(matrix, length):
  """This is the front-end function.  It returns the maximum product of "length" consecutive
  entries, either along the rows, columns, or diagonals."""

  row_max  = max_row_product(matrix, length)
  col_max  = max_row_product(zip(*matrix), length)  #NB:  xip(*matrix) is the transpose
  diag_max = max_diag_product(matrix, length)

  print "(r, c, d) = ({0}, {1}, {2})".format(row_max, col_max, diag_max)
  return max([row_max, col_max, diag_max])


if __name__ == "__main__":
  matrix = load_matrix("problem11.dat")
  answer = find_max(matrix, 4)
  print "The maximum product is {0}".format(answer)
