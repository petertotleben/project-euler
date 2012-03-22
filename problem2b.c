/* Project Euler -- Problem 2 
 *
 * Find the sum of all the even-valued terms in the Fibonacci sequence
 * which do not exceed four million.
 *
 * But this is the first shortcut, it is precicely the terms which are
 * multiples of three that are even, so we only need those.
 *
 * And there is a further speedup, for it can be shown that in the 
 * Fibonacci sequence
 *     F(n) = 4*F(n-3) + F(n-6)
 *
 */

#include <stdio.h>

int main()
{
  long int three_back = 2;
  long int six_back = 0;
  long int current = 4*three_back + six_back;
  long int sum = 2;  // We're skipping F(3), so add it here.

  while(current <= 4000000) {
    sum += current;
    six_back = three_back;
    three_back = current;
    current = 4*three_back + six_back;
  }

  printf("The answer is %d\n", sum);

  return 0;
}
