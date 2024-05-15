//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
class GfG
{
    public static void main(String args[])
        {
            Scanner sc = new Scanner(System.in);
            int t = sc.nextInt();
            while(t-->0)
                {
                    int n = sc.nextInt();
                    int m = sc.nextInt();
                    int a[] = new int[n];
                    int b[] = new int[m];
                    for(int i = 0;i<n;i++)
                        a[i] = sc.nextInt();
                    for(int i = 0;i<m;i++)
                        b[i] = sc.nextInt();    
                    Solution ob = new Solution();
                    System.out.println(ob.maxDotProduct(n, m, a, b));
                }
        }
}    
// } Driver Code Ends


//User function Template for Java
class Solution
{
    public int fun(int i, int j, int [] a, int [] b, int elem, int [][] dp){
        int n = a.length, m = b.length;
        
        if(i>=n ) return 0;
        if(j>=m) return 0;
        
        if(dp[i][j] != -1) return dp[i][j];
        
        int first=0, second =0;
        first = a[i]*b[j] + fun(i+1, j+1, a, b, elem, dp);
        if(elem>0) second= fun(i+1, j, a, b, elem-1, dp);
        
        return dp[i][j] = Math.max(first, second);
        
    }
    
	public int maxDotProduct(int n, int m, int a[], int b[]) 
	{ 
	    int [][] dp = new int[n+1][m+1];
	    for(int i=0; i<dp.length; i++){
	        for(int j=0; j<dp[0].length; j++) dp[i][j] = -1;
	    }
		return fun(0, 0, a, b, n-m, dp);
	} 
}