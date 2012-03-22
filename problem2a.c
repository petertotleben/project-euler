/* Project Euler -- Problem 2 
 *
 * Find the sum of all the even-valued terms in the Fibonacci sequence
 * which do not exceed four million.
 *
 * But this is the first shortcut, it is precicely the terms which are
 * multiples of three that are even, so we only need those.
 *
 */

#include <stdio.h>

int main()
{
  long int two_back = 1;
  long int one_back = 1;
  long int current = two_back + one_back;
  long int sum = 0;

  while(current <= 4000000) {
    sum += current;
    two_back = current + one_back;
    one_back = two_back + current;
    current = two_back + one_back;
  }

  printf("The answer is %d\n", sum);

  return 0;
}
