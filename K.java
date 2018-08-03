import java.util.*;

public class K {

  public static int getKthLargest( int arr[], int k ) {
    Arrays.sort( arr );
    return arr[ arr.length - k ];
  }

  public static void main( String[] args ) {
    int arr[] = {9, 1, 3, 5, 11};
    int k = 2;
    int result = getKthLargest( arr, k );
    System.out.println( "[+] result should be 9, and it is: " + result );
  }
}
