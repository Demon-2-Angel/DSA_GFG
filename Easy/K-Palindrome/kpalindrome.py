#User function Template for python3

class Solution:
    def kPalindrome(self, str, n, k):
        dp = [[-1] * n for _ in range(n)]
        longest_palindromic_subseq_length = self.solve(0, n - 1, str, dp)
        if (n - longest_palindromic_subseq_length) <= k:
            return 1
        else:
            return 0
    
        # code here
    def solve(self, l, r, s, dp):
        if l > r:
            return 0
        if l == r:
            return 1
        if dp[l][r] != -1:
            return dp[l][r]

        if s[l] == s[r]:
            dp[l][r] = 2 + self.solve(l + 1, r - 1, s, dp)
        else:
            dp[l][r] = max(self.solve(l + 1, r, s, dp), self.solve(l, r - 1, s, dp))

        return dp[l][r]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        n = int(arr[0])
        k = int(arr[1])
        str = input()

        ob = Solution()
        print(ob.kPalindrome(str, n, k))

# } Driver Code Ends