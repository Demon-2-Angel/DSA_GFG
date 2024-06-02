
from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        # code here
        mpp = {}
        ans = [0]
        for i in range(q):
            qtype = queries[i][0]
            qval = queries[i][1]
            if qtype == 0:
                ans.append(qval)
            else:
                ind = len(ans) -1
                if ind in mpp.keys():
                    mpp[ind] ^= qval
                else: mpp[ind] = qval
        
        n = len(ans)
        xorVal = 0
        for i in range(n-1, -1, -1):
            if i in mpp.keys():
                xorVal ^= mpp[i]
            ans[i] ^= xorVal
        return sorted(ans)

#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


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

        q = int(input())

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.constructList(q, queries)

        IntArray().Print(res)

# } Driver Code Ends