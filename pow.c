/**
 * @file pow.c
 * @author Will Rabb (wirabb)
 *
 * This file contains the code to take the exponent of a number; given the number and the exponent
 */

#include <stdio.h>
#include <stdlib.h>

/**
 * This function provides a way to take the exponent of a number
 *
 * @param num - the number to take the exponent of
 * @param toThePowerOf - the number of times to multiple num by itself
 *
 * @return result - the number after the operation is performed; effectively num^toThePowerOf
 */
int myPow( int num, int toThePowerOf ) {
  int result = 1;
  for ( int i = 0; i < toThePowerOf; i++ ) {
    result *= num;
  }
  return result;
}

/**
 * This function runs the program
 *
 * @param argc - the number of command line arguments given
 * @param argv - the command line arguments in a list of strings
 *
 * @return the exit status of the program
 */
int main( int argc, char *argv[] ) {
  printf("[+] 2^8 = 256, we actually received %d\n", myPow(2, 8));
  return EXIT_SUCCESS;
}
