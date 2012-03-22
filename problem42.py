#!/usr/bin/python
#
# Project Euler Problem 42
#
# How many triangle words are in problem42.dat?
#
# A triangle word is a word whose letter sums add up to a triangle number

def read_file(filename):
  try:
    handle = open(filename, "r")
    wordlist = handle.read().split(",")
    wordlist = [item.strip(r'"') for item in wordlist]
  except IOError as (errno, strerr):
    print "There was an error reading {0}:  {1}".format(filename, strerr)
  finally:
    handle.close()

  return wordlist



def word_score(word):
    score = 0
    for i in range(len(word)):
        score += (ord(word[i])-64)
    return score



def gen_triangle_num_list(n):
    numlist = [0]
    for i in range(1, n+1):
        numlist.append(numlist[i-1] + i)
    return numlist



def main(filename):
    num_words = 0
    triangle_nums = gen_triangle_num_list(5000)
    word_list = read_file(filename)
    for word in word_list:
        if word_score(word) in triangle_nums:
            num_words += 1
    return num_words



if __name__ == "__main__":
    answer = main("problem42.dat")
    print "The answer is {0}".format(answer)
