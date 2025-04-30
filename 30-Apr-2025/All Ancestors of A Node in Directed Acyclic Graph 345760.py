# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for i in edges:
            x,y = i
            graph[y].append(x)
        ans = []
        temp = set()
        def dfs(i):
            for j in graph[i]:
                if j not in temp:
                    temp.add(j)
                    dfs(j)
        for i in range(n):
            dfs(i)
            ans.append(sorted(list(temp)))
            temp = set()
        return ans
        