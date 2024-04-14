//{ Driver Code Starts
import java.util.*;

public class GFG {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int arr[] = new int[n];
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            Solution obj = new Solution();
            obj.xor1ToN(n, arr);
            obj.printArr(n, arr);
            obj.setToZero(n, arr);
            obj.printArr(n, arr);
        }
        sc.close();
    }
}

// } Driver Code Ends


// User function Template for Java
class Solution {
    // Method to print an array
    public void printArr(int n, int arr[]) {
        // Loop through the array and print each element
        for(int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
        // Print a newline character after printing the array
        System.out.println();
    }

    // Method to set all elements of the array to zero
    public void setToZero(int n, int arr[]) {
        // Loop through the array and set each element to zero
        for(int i = 0; i < n; i++) {
            arr[i] = 0;
        }
    }

    // Method to perform XOR operation with index on each element of the array
    public void xor1ToN(int n, int arr[]) {
        // Loop through the array
        for(int i = 0; i < n; i++) {
            // Perform XOR operation with the index and assign the result to the element
            arr[i] ^= i;
        }
    }
}