import java.util.*;

public class BinaryTree {

  public String visitNode( Node toVisit, String visited ) {
    if ( toVisit == null ) {
      return visited;
    }
    visited += " " + toVisit.val;
    String leftVisit = visitNode( toVisit.left, visited );
    String rightVisit = visitNode( toVisit.right, visited );
    if ( leftVisit.equals( rightVisit ) ) {
      return leftVisit;
    }
    return leftVisit + " & " + rightVisit;
  }

  public void findLeaves( Node root ) {
    System.out.println( visitNode( root, "" ) );
  }

  public void run() {
    Node neg7 = new Node( -7, null, null );
    Node negOne = new Node( -1, null, null );
    Node negTwo = new Node( -2, neg7, negOne );
    Node three = new Node( 3, null, null );
    Node head = new Node( 0, negTwo, three );
    findLeaves( head );
  }

  public static void main( String[] args ) {
    BinaryTree tree = new BinaryTree();
    tree.run();
  }

  public class Node {
    public int val;
    public Node left;
    public Node right;

    public Node( int val, Node left, Node right ) {
      this.val = val;
      this.left = left;
      this.right = right;
    }
  }
}
