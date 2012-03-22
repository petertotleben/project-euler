/* Project Euler -- Problem 3
 *
 * What is the largest prime factor of 600851475143
 *
 */

int true = 1;
int false = 0;

#include<stdio.h>
#include<math.h>
#include<stdlib.h>


/* Returns true iff n is a positive prime integer */
int isPrime(long long int n)
{
  if (n == 2) return true;

  long long search_limit = (long long) floor(sqrt((double) n));
  long long i;

  for (i=3; i<=search_limit; i+=2) {
    if ( (n % i) == 0 ) return false;
  }

  return true;
}


int main(void)
{
  long long n = 600851475143LL;
  long long search_limit =  (long) floor(sqrt((double) n));
  long long int i;

  /* NB:  Since we are dividing out factors as we find them, 
   * we do not need to check if they are each prime, because
   * this will happen automatically
   */

  for (i=3; i<=search_limit; i+=2) {
    if ( (n % i) == 0 ) {
      n /= i;
      printf("\nPrime factor: %d\n", i);
    }
  }
  
  printf("done.\n");
  
  return 0;
}
