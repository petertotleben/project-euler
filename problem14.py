# Project Euler Problem 14
#
# Find the longest Collatz chain with a starting term under 1,000,000

def next_in_sequence(n):
  if n % 2 == 0:
    return n/2
  else:
    return 3*n + 1


def count_collatz_chain(first_num):
  i = 1
  term = first_num
  while (term != 1):
    term = next_in_sequence(term)
    i+=1
  return i

def main(max_num_to_try):
  max_start_number = 0
  max_chain_length = 0
  for i in range(2, max_num_to_try):
    length = count_collatz_chain(i)
    if length > max_chain_length:
      max_chain_length = length
      max_start_number = i
  return max_start_number


if __name__ == "__main__":
  answer = main(1000000)
  print "The answer is {0}".format(answer)

