#User function Template for python3

class Solution:

    def CountPS(self, s, n):
        # code here
        
        c = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    string = s[i : j+1]
                    if string == string[::-1]:
                        c += 1
        
        return c
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.CountPS(S, N))

# } Driver Code Ends