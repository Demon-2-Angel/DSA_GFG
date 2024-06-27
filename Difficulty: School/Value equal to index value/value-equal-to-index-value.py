#User function Template for python3
class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		
        if n==0:
            return 0
        elif n>0:
            k =[]
            for i in range(0,n):
                if arr[i]==i+1:
                    k.append(arr[i])
        return k
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends