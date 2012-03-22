#!/usr/bin/python
#
# Problem 19 -- How many times did the first of the month fall on a Sunday in the twentieth century

class DayOfWeek:
  day = 1 

  def advance(self):
    self.day = (self.day + 1) % 7



class Date:
  year = 1900
  month = 1
  day = 1

  def advance(self):
    if (self.month == 12):
      if (self.day == 31):
        self.year += 1
        self.month = 1
        self.day = 1
      else:
        self.day +=1
    elif (self.month == 9) or (self.month == 4) or (self.month == 6) or (self.month == 11):
      if (self.day == 30):
        self.month +=1
        self.day = 1
      else:
        self.day += 1
    elif (self.month == 2):
      if (self.day == 28):
        if (self.year % 100 == 0) and (self.year % 400 == 0):
          self.day += 1
        elif (self.year % 4 == 0):
          self.day += 1
        else:
          self.day = 1
          self.month += 1
      elif (self.day == 29):
        self.day = 1
        self.month += 1
      else:
        self.day += 1
    else:
      if (self.day == 31):
        self.day = 1
        self.month += 1
      else:
        self.day += 1


def main():
  day_of_week = DayOfWeek()
  date = Date()

  answer = 0

  while (date.year != 2001):
    if (date.year >= 1901):
      print "{0}/{1}/{2}  Day of week:  {3}".format(date.year, date.month, date.day,
          day_of_week.day)
      if (date.day == 1) and (day_of_week.day == 0):
        answer += 1
    day_of_week.advance()
    date.advance()

  return answer



if __name__ == "__main__":
  answer = main()
  print "The answer is {0}".format(answer)
