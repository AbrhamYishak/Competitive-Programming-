# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = defaultdict(list)
        for i in edges:
            a,b = i
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        def dfs(curr):
            if curr == destination:
                return True
            for i in graph[curr]:
                if i in visited:
                    continue
                visited.add(i)
                if dfs(i):
                    return True
            return False
        return dfs(source)
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        