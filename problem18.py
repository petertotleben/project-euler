# Project Euler Problem 18
#
# Find the path through the triangle in problem18.dat with the maximal sum

def read_file(filename):
  try:
    handle = open(filename, "r")
    lines = handle.readlines()
  except IOError as (errno, strerr):
    print "There was an error reading {0}:  {1}".format(filename, strerr)
  finally:
    handle.close()

  return [ map(int, line.split()) for line in lines ]



def lattice_sum_iterative(lattice):
  for i in range(len(lattice)-2, -1, -1):
    for j in range(0, i + 1):
      lattice[i][j] = lattice[i][j] + max(lattice[i+1][j], lattice[i+1][j+1])
  return lattice[0][0]


if __name__ == "__main__":
  lattice = read_file("problem67.dat")
  answer = lattice_sum_iterative(lattice)
  print "The answer is {0}".format(answer)


