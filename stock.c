#include <stdio.h>
#include <stdlib.h>

/**
 * This function finds the maximum profit you can make by buying a stock on a certain day and selling it on a specified day
 *
 * @param stocks - the array of stock prices
 * @param size   - the size of the array
 *
 * @return the maximum profit
 */
int findProfit(int stocks[], int size) {
  int max = stocks[1] - stocks[0];
  int min = stocks[0];
  /**for ( int i = 0; i < size; i++ ) {
    for ( int j = i + 1; j < size; j++ ) {
      int diff = stocks[j] - stocks[i];
      if ( diff >= maxDiff ) {
        maxDiff = diff;
      }
    }
  }
  */
  for ( int i = 0; i < size; i++ ) {
    if ( stocks[i] < min ) {
      min = stocks[i];
    } else {
      if ( stocks[i] - min > max ) {
        max = stocks[i] - min;
      }
    }
  }
  return max;
}

int main(int argc, char *argv[]) {
  int mine[] = {7, 1, 6, 5, 2};
  int result = findProfit(mine, 5);
  printf("Expected: %d, Actual Result: %d\n", 5, result);
  return EXIT_SUCCESS;
}
