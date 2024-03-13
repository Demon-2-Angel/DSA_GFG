//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            int n = Integer.parseInt(br.readLine().trim());
            int[][] mat = new int[n][n];
            String[] S = br.readLine().trim().split(" ");
            int i = 0;
            int j = 0;
            for(int k = 0; k < S.length; k++){
                mat[i][j] = Integer.parseInt(S[k]);
                j++;
                if(j == n){
                    i++;
                    j = 0;
                }
            }
            Solution obj = new Solution();
            int[] ans = obj.matrixDiagonally(mat);
            for(int it = 0; it < ans.length; it++){
                System.out.print(ans[it] + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


class Solution {
public int[] matrixDiagonally(int[][] mat) {
        int n = mat.length;
        if(n==1) return mat[0];
        int[] ans = new int[n*n];
        int count = 0;
        int r=0;
        int c=0;
        while(r<n && c<n && count<(n*n)){
            //System.out.println(mat[r][c]+" r="+r+" c="+c);
            ans[count++] = mat[r][c];
            if((r+c)%2==0){
                r--;
                c++;
                if(c==n){c--; r+=2;}
                if(r==-1) r++;
            }else{
                r++;
                c--;
                if(r==n) {r--; c+=2;}
                if(c==-1) c++;
            }
        }
        return ans;
}
}