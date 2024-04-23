//{ Driver Code Starts
// Initial Template for Java
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            int n = Integer.parseInt(read.readLine());
            Solution ob = new Solution();
            System.out.println(ob.firstElement(n));
        }
    }
}
// } Driver Code Ends


class Solution {
    static int firstElement(int n) {
        int mod = 1000000007;
        int a = 1, b=1;
        int c = a+b;
        int i=1;
        while(i<n){
            a = b;
            b = c;
            c = (a%mod+b%mod)%mod;
            i++;
        }
        return a;
    }
}