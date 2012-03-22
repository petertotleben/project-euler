/* Project Euler -- Problem 7
 *
 * Find the 1001st prime
 *
 */

#include<stdio.h>
#include<math.h>

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

int main()
{
  long num_primes = 10001;  /* Number of primes to find */
  long current_number = 2;
  long primes_found = 0;

  while (primes_found < num_primes) {
    if(isPrime(current_number)) {
      primes_found++;
      printf("%d.\t%d\n", primes_found, current_number);
    }
    current_number++;
  }

  return 0;
}

      
