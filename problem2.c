/* Project Euler -- Problem 2 
 *
 * Find the sum of all the even-valued terms in the Fibonacci sequence
 * which do not exceed four million.
 *
 */

#include <stdio.h>

int main()
{
  long int two_back = 1;
  long int one_back = 1;
  long int current;
  long int sum = 0;

  do {
    current = two_back + one_back;
    if ( (current % 2) == 0)
      sum += current;
    two_back = one_back;
    one_back = current;
  } while (current <= 4000000);

  printf("The answer is %d\n", sum);

  return 0;
}
