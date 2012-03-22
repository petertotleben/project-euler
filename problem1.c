/* Project Euler -- Problem 1
 *
 * Find the sum of all the multiples of 3 or 5 below 1000
 */

#include<stdio.h>

int main()
{
  long int sum = 0;
  int i;
 
  for (i=0; i<1000; i++)
    {
      if ( ((i % 3) == 0) || ((i % 5) == 0) )
	sum += i;
    }

  printf("The sum is %d\n", sum);

  return 0;
}
