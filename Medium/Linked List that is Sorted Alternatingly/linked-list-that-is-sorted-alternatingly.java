//{ Driver Code Starts
/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class Node {
    int data;
    Node next;
    
    public Node (int data){
        this.data = data;
        this.next = null;
    }
}

class GFG {
    static void printList(Node node) 
	{ 
		while (node != null) 
		{ 
			System.out.print(node.data + " "); 
			node = node.next; 
		} 
		System.out.println(); 
	}
	public static void main (String[] args) {
		Scanner sc  = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-- > 0){
		    int n = sc.nextInt();
		    
		    Node head = new Node(sc.nextInt());
		    Node tail = head;
		    
		    for(int i=1; i<n; i++){
		        tail.next = new Node(sc.nextInt());
		        tail = tail.next;
		    }
		    Solution obj = new Solution();
		    head = obj.sort(head);
		    printList(head);
		}
	}
}

// } Driver Code Ends



/*
class Node {
    int data;
    Node next;
    
    public Node (int data){
        this.data = data;
        this.next = null;
    }
}
*/

class Solution {
    
    public Node reverse(Node head){
        Node cur = head;
        Node prev = null;
        
        while (cur!= null) {
            Node next = cur.next;
            cur.next = prev;
            prev = cur;
            cur = next;
        }
        
        return prev;
    }
    
   public Node sort(Node head){
        //your code here, return the head of the sorted list
        
        Node slow = head;
        Node fast = slow.next;
        
        Node h1 = slow;
        Node h2 = fast;
        
        while (fast != null && slow != null){
            slow.next = fast.next;
            if (fast.next != null)
                fast.next = fast.next.next;
                
            slow = slow.next;
            fast = fast.next;
        }
        
        h2 = reverse(h2);
        
        slow = h1;
        while (slow.next != null)
            slow = slow.next;
        slow.next = h2;
        return h1;
   }
   


}