# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in edges:
            a,b = i
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        print(graph)
        def bfs(i):
            q = deque()
            q.append(i)
            nodes = len(graph[i])
            complete = True
            start = len(visited)
            while q:
                for _ in range(len(q)):
                    a =q.popleft()
                    if len(graph[a])!=nodes:
                        complete = False
                    for j in graph[a]:
                        if j not in visited:
                            visited.add(j)
                            q.append(j)
            if len(visited)-start!=nodes:
                return False
            return complete
        count = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                if bfs(i):
                    count+=1
        return count
