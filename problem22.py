# Project Euler #22
#
# Sum of name scores.
# NB:  A name score is the sum of the digit-values of the names times the order it is on the list

def read_file(filename):
  try:
    handle = open(filename, "r")
    namelist = handle.read().split(",")
    namelist = [item.strip(r'"') for item in namelist]
    namelist.sort()
  except IOError as (errno, strerr):
    print "There was an error reading {0}:  {1}".format(filename, strerr)
  finally:
    handle.close()

  return namelist



def name_score(name):
    score = 0
    for i in range(len(name)):
        score += (ord(name[i])-64)
    return score



def sum_of_scores(namelist):
    sum = 0
    for i in range(len(namelist)):
        sum += ((i+1) * name_score(namelist[i]))
    return sum



if __name__ == "__main__":
    name_list = read_file("problem22.dat")
    answer = sum_of_scores(name_list)
    print "The answer is {0}".format(answer)
