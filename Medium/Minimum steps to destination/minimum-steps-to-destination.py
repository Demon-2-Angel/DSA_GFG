#User function Template for python3

class Solution:
    def minSteps(self, d):
        # code here
        ans = 0
        temp = 0
        while temp < d:
            ans += 1
            temp += ans
        if temp == d:
            return ans
        diff = temp - d
        if diff%2 == 0 :
            return ans
        if ans%2 == 0:
            return ans + 1
        else :
            return ans + 2

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

# } Driver Code Ends