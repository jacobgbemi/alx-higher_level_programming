#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <unistd.h>
#include <math.h>

/* Program to find the largest palindrome number which
 * is product of two n digit numbers
 */


/**
 * largest_palindrome - calculate largest palindrome 
 * which is product of two n-digits numbers
 * @n: number of digits
 * Return: the product
 */
int largest_palindrome(int n)
{
  int i, lower_limit, upper_limit, product, reverse, number;
  int j, max_product;

  upper_limit = pow(10,n) - 1;
  /* largest number of n-1 digit.
  * One plus this number is lower
  * limit which is product of two numbers.
  */
  lower_limit = 1 + upper_limit / 10;

  /* Initialize result*/
  max_product = 0;
  for (i = upper_limit;
      i >= lower_limit;
      i--)
  {
    for (j = i; j >= lower_limit; j--)
    {
      /* calculating product of two n-digit numbers*/
      product = i * j;
      if (product < max_product)
        break;
      number = product;
      reverse = 0;

      /* calculating reverse of product to check whether
       * it is palindrome or not
       */
      while (number != 0)
      {
        reverse = reverse * 10 +
            number % 10;
        number /= 10;
      }

      /* update new product if exist and if greater than previous one*/
      if (product == reverse &&
        product > max_product)
        
        max_product = product;
    }
  }
  return max_product;
}

/* Driver code*/
int main()
{
  int n = 2;
  int number = largest_palindrome(n);
  printf(number);
  return 0;
}

