# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        q = deque()
        seen = [[0 for j in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i,j))
                    seen[i][j] = 1
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        level = -1
        while q:
            for i in range(len(q)):
                a = q.popleft()
                x,y = a
                for j in direction:
                    x1,y1 = j
                    if -1<x1+x<r and -1<y1+y<c and seen[x+x1][y+y1]==0 and grid[x+x1][y+y1]!=0:
                        q.append((x+x1,y+y1))
                        seen[x+x1][y+y1] = 1
            level+=1
        for i in range(r):
            for j in range(c):
                if seen[i][j] == 0 and grid[i][j]!=0:
                    return -1
        if level == -1:
            return 0
        return level
                
