
from typing import List
from collections import defaultdict

class Solution:
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        # code here
        # code here
        
        graph = defaultdict(list)
        for fro, to in edges:
            graph[fro].append(to)
            graph[to].append(fro)
            
        def dfs(vertex, nei):
            nonlocal flag, count
            vis.add(vertex)
            count += 1
            if len(graph[vertex]) != nei:
                flag = False
            for n in graph[vertex]:
                if n not in vis:
                    dfs(n, nei)
            flag = flag & True
        ans = 0
        vis = set()
        for i in range(1, v+1):
            # print(vis)
            nei = len(graph[i])
            count = -1
            flag = True
            if i not in vis:
                dfs(i, nei)
                # print(count)
                if flag and count == nei:
                    # print(i)
                    ans += 1
        return ans    
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

        e = int(input())

        v = int(input())

        edges = IntMatrix().Input(e, 2)

        obj = Solution()
        res = obj.findNumberOfGoodComponent(e, v, edges)

        print(res)

# } Driver Code Ends