/* Project Euler -- Problem 6 
 *
 * Find the difference between the sum of the squares and the 
 * square of the sum of the first 100 integers
 */

#include <stdio.h>

int main()
{
  long n = 100;
  long sum = (n * (n+1)) / 2;
  long square_of_sum = sum * sum;
  long sum_of_squares = ( n * (n+1) * (2*n + 1) ) / 6;
  long answer = square_of_sum - sum_of_squares;
  printf("The answer is %d\n", answer);
  return 0;
}
