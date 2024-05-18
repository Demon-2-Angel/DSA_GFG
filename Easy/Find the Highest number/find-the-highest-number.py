#User function Template for python3
from typing import List

class Solution:
    def findPeakElement(self, a):
        n=len(a)
        l,h=0,n-1
        while l<=h:
            mid=(l+h)//2
            if mid>0 and a[mid-1]>a[mid]:
                h=mid-1
            elif mid+1==n or a[mid]>a[mid+1]:
                return a[mid]
            else:
                l=mid+1
		# Code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findPeakElement(a)
        print(ans)

# } Driver Code Ends