#User function Template for python3

class Solution:
    
    # Function to find maximum of each subarray of size k.
    def max_of_subarrays(self, arr, n, k):
        if n < k or k <= 0:
            return -1
        
        result = []
        dq = deque()
        
        for i in range(n):
            # Remove elements not within the sliding window
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # Remove elements smaller than the current element from the deque
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            
            # Add the current element index at the end of the deque
            dq.append(i)
            
            # The front of the deque contains the maximum element for the current window
            if i >= k - 1:
                result.append(arr[dq[0]])
        
        return result


# Example usage:
# obj = Solution()
# result = obj.max_of_subarrays([1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 3)
# print(result)  # This should output the sums of all subarrays of size 3



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends