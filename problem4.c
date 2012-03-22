/*
 * Project Euler -- Problem 4
 *
 * Find the largest palindrome made from the poduct of two
 * three-digit numbers
 *
 */
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

const int FALSE = 0;
const int TRUE = 1;
const int MAX_DIGITS = 8;



int is_palindrome(char *num_str, int left_index, int right_index)
{
  if (left_index == right_index) 
    {
      return TRUE;
    }
  else if ( left_index == (right_index - 1) )
    {
      if (num_str[left_index] == num_str[right_index])
	return TRUE;
      else
	return FALSE;
    }
  else 
    {
      if (num_str[left_index] == num_str[right_index])
	return is_palindrome(num_str, left_index + 1, right_index - 1);
      else
	return FALSE;
    }
}


int main()
{
  long i, j;
  long largest_palindrome = 0;
  long current_num;
  char current_num_str[MAX_DIGITS];

  for (i=100; i<=999; i++)
    for (j=i; j<=999; j++)
      {
	current_num = i*j;
	sprintf(current_num_str, "%ld", current_num);
	int length = strlen(current_num_str);
	if (is_palindrome(current_num_str, 0, length-1))
	  if (current_num > largest_palindrome)
	    largest_palindrome = current_num;
      }

  printf("The answer is %ld\n", largest_palindrome);
  return 0;
}
