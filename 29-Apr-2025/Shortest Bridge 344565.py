# Problem: Shortest Bridge - https://leetcode.com/problems/shortest-bridge/

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        comp = [[0 for j in range(c)] for k in range(r)] 
        q = deque()
        def dfs(i,j):
            comp[i][j] = 1
            for k in direction:
                i1,j1 = k
                if -1<i+i1<r and -1<j+j1<c and comp[i+i1][j+j1]!=1 and grid[i+i1][j+j1] == 1:
                    dfs(i+i1,j+j1)
        for i in range(r):
            done = False
            for j in range(c):
                if grid[i][j] == 1:
                    dfs(i,j)
                    done = True
                    break
            if done:
                break
        for i in range(r):
            for j in range(c):
                if comp[i][j] == 1:
                    q.append((i,j))
        level = 0
        while q:
            add = False
            done = False
            for _ in range(len(q)):
                a = q.popleft()
                i,j = a
                for k in direction:
                    i1,j1 = k
                    if -1<i+i1<r and -1<j+j1<c and comp[i+i1][j+j1]!=1 and grid[i+i1][j+j1] == 0:
                        add = True
                        comp[i+i1][j+j1] = 1
                        grid[i+i1][j+j1] = 1
                        q.append((i+i1,j+j1))
                    elif -1<i+i1<r and -1<j+j1<c and comp[i+i1][j+j1]!=1 and grid[i+i1][j+j1] == 1:
                        return level
            if add:
                level+=1
            
