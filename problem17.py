#!/usr/bin/python
#
# Project Euler Problem 17
#
# How many letters are in the numbers from 1 to 1000 spelled out?

ones_names = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
"eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
"nineteen"]

tens_names = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
"ninety"]


def spell_number(n):
  if (n < 20):
    return ones_names[n]
  elif (n == 1000):
    return "onethousand"
  else:
    spelled_number = ""
    ones = n % 10
    n /= 10
    tens = n % 10
    n /= 10
    hundreds = n % 10
    if (hundreds):
      spelled_number += (ones_names[hundreds] + "hundredand")
    if (tens == 1):
      return spelled_number + ones_names[(tens*10)+ones]
    if (tens > 1):
      spelled_number += tens_names[tens]
    if (ones):
      spelled_number += ones_names[ones]
    return spelled_number



def main():
  total_letters = 0
  for i in range (1, 1001):
    spelled_name = spell_number(i)
    length = len(spelled_name)
    print "i={0}\t{1}\tlength: {2}".format(i, spelled_name, length)
    total_letters += length
  return total_letters



if __name__ == "__main__":
  answer = main()
  print "The answer is {0}".format(answer)
