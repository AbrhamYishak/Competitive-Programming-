# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution(object):
    def islandPerimeter(self, grid):
        visited = set()
        row = len(grid)
        col = len(grid[0])
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        def validate(i,j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            elif grid[i][j] == 0:
                return False
            return True
        visited = set()
        def dfs(i,j):
            visited.add((i,j))
            ans = 0
            for k in direction:
                a,b = k
                if (i+a,j+b) in visited:
                    continue
                if validate(i+a,j+b):
                    ans += dfs(i+a,j+b)
                else:
                    ans += 1
            return ans
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return dfs(i,j)
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        