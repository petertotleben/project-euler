/* Project Euler -- Problem 12
 *
 * This program finds the first triangle number to have over MIN_NUM_DIV divisors
 *
 */

#include<stdlib.h>
#include<stdio.h>
#include<math.h>

#define MIN_NUM_DIV 500

void populate_prime_exponent_array(long long int n, long long int *prime_exponent_array)
{
  int index=0;
  int i;
  long long int search_limit = (long long int) floor(sqrt((double) n));

  for (i=2; i<=search_limit; i++)
    {
      int exponent=0;
      while( (n % i) == 0 ) 
      {
	     exponent++;
	     n /= i;
	  }
      prime_exponent_array[index] = exponent + 1;
      index++;
    }

  prime_exponent_array[index] = -1;
}
  

long long int num_divisors(long long int n)
{
  long long int *prime_exponent_array = NULL;
  long long int number_of_divisors = 1;
  long long int i = 0;

  prime_exponent_array = (long long int *) malloc((MIN_NUM_DIV + 2) * sizeof(long long int));
  populate_prime_exponent_array(n, prime_exponent_array);

  while(prime_exponent_array[i] != -1) 
    {
      number_of_divisors *= prime_exponent_array[i];
      i++;
    }
  
  free(prime_exponent_array);
  return number_of_divisors;
}

long long int triangle_num(long long int n)
{
   return  ( n * (n+1) ) / 2;
}

int main()
{
  long long int n=0;
  long long int number_of_divisors = 0;

  while(number_of_divisors < MIN_NUM_DIV)
    {
      number_of_divisors = num_divisors(triangle_num(n));
      n++;
    }
  
  printf("The answer is %lld which has %lld divisors\n", triangle_num(n-1), number_of_divisors);
}
	
