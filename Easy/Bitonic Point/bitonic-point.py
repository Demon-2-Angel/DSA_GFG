#User function Template for python3
class Solution:

	def findMaximum(self,arr, n):
		# code here
        if n == 1:
            return arr[0]
        elif arr[n-1] > arr[n-2]:
            return arr[n-1]
        else:
            low = 0
            high = n - 1
            
            while low<= high:
                mid = high + low // 2
                if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                    return arr[mid]
                elif arr[mid] > arr[mid - 1]:
                    low = mid + 1
                else:
                    high = mid - 1
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends