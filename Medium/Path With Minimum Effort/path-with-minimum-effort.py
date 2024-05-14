
from typing import List
import heapq

class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        # code here
        hth=len(heights)
        wth=len(heights[0])
        dp=[[float('inf') for _ in range(wth)] for _ in range(hth)]
        dp[0][0]=0
        q=[(0,0,0,)]
        while q:
            mx,x,y=heapq.heappop(q)
            for dx,dy in [(-1,0,),(1,0,),(0,-1,),(0,1,)]:
                nx,ny=x+dx,y+dy
                if not(0<=nx<wth and 0<=ny<hth):
                    continue
                mn=min(dp[ny][nx],max(mx,abs(heights[y][x]-heights[ny][nx])))
                if mn<dp[ny][nx]:
                    dp[ny][nx]=mn
                    heapq.heappush(q,((mn,nx,ny,)))
        return dp[-1][-1]





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


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        rows = int(input())

        columns = int(input())

        heights = IntMatrix().Input(rows, columns)

        obj = Solution()
        res = obj.MinimumEffort(rows, columns, heights)

        print(res)

# } Driver Code Ends