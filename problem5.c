/* Project Euler -- Problem 5
 *
 * Find the smallest integer evenly divisible by 1, 2, ..., 20
 *
 * We just need to multiply all the prime powers less than or 
 * equal to 20.
 */

#include <stdio.h>
#include <math.h>

const int true = 1;
const int false = 0;


int isPrime(long n)
{
  if (n == 2) return true;             /* take care of the only even prime */
  if ( (n%2) == 0 ) return false;

  long limit = (long) sqrt((double) n);
  long i;

  for (i=3; i<=limit; i+=2)
      if ( (n % i) == 0 ) return false;

  return true;
}

/* given prime p, this returns highest power <= n */
long max_prime_power(long p, long n)
{
  long answer = 1;
  while ( (answer * p) <= n)
    answer *= p;
  return answer;
}

int main()
{
  long n = 10;
  long i;
  long answer = 1;

  for(i=2; i<=n; i++)
    {
      if (isPrime(i)) {
	answer *= max_prime_power(i, n);
	printf("i=%d power=%d answer=%d\n", i, max_prime_power(i,n), answer);
      }
    }

  printf("Answer is %d\n", answer);
  return 0;
}
