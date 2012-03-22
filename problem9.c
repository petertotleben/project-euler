/*
 * Project Euler -- Problem 9
 *
 * Find the product of the Pythagorean Triple whose sum is 1000.
 *
 */

#include<stdio.h>

const int TRUE = 1;
const int FALSE = 0;

int isTriple(int a, int b, int c)
{
  if ( (a*a + b*b) == (c*c) )
    return 1;
  else
    return 0;
}

int main()
{
  int a, b, c;

  for (a=1; a<1000; a++) {
    for (b=(a+1); b<1000; b++) {
      c = 1000 - a - b;
      if (c < 0) continue;
      if (isTriple(a, b, c)) {
		printf("The answer:  a=%d b=%d c=%d abc=%d\n", a, b, c, a*b*c);
		break;
      }
    }
  }
}
