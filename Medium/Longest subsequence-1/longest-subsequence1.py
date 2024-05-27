
from typing import List


class Solution:
    def longestSubseq(self, n : int, a : List[int]) -> int:
        # code here
        prv = dict()
        mx = 0
        for i in a:
            prv[i] = max(prv.get(i,1), prv.get(i-1, -1) + 1, prv.get(i+1, -1) +1)
            mx = max(mx, prv[i])
        return mx



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        a = IntArray().Input(n)

        obj = Solution()
        res = obj.longestSubseq(n, a)

        print(res)

# } Driver Code Ends