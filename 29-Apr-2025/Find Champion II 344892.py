# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in edges:
            x,y = i
            graph[y].append(x)
        ans = []
        for i in range(n):
            if not graph[i]:
                ans.append(i)
        if len(ans) > 1:
            return -1
        else:
            return ans[0]