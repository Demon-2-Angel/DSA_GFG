//{ Driver Code Starts
//Initial template for JAVA

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG
 {
	public static void main (String[] args) throws IOException
	 {
	    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	    int t = Integer.parseInt(br.readLine());
	    for(int i=0;i<t;i++){
	        int n = Integer.parseInt(br.readLine());
	        String l = br.readLine();
    		String[] sarr = l.split(" ");
    		int[] arr = new int[sarr.length];
    		for(int i1=0;i1<arr.length;i1++){
    			arr[i1] = Integer.parseInt(sarr[i1]);
    		}
    		
            Solution obj = new Solution();
            
            int[] res = obj.twoRepeated(arr, n);
            System.out.println(res[0] + " " + res[1]);
	    }
	}
}
// } Driver Code Ends

class Solution {
    // Function to find two repeated elements.
    public int[] twoRepeated(int arr[], int n) {
        Set<Integer> set = new HashSet<>();
        int[] result = new int[2]; // Array to store the repeating numbers
        int index = 0; // Index to keep track of which repeating number to store
        
        for (int i = 0; i < n + 2; i++) {
            if (!set.add(arr[i])) {
                result[index++] = arr[i]; // Store the repeating number in the result array
                if (index == 2) {
                    break; // Found both repeating numbers, no need to continue
                }
            }
        }
        
        return result;
    }
}