# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        ans = 0
        row = len(grid)
        col = len(grid[0])
        path = set()
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def validate(i,j):
            if i < 0 or j < 0 or i >= row or j >= col:
                return False
            elif grid[i][j] == "0":
                return False
            return True
        def dfs(i,j):
            path.add((i,j))
            for k in dir:
                a,b = k
                if (i+a,j+b) in path:
                    continue
                if validate(i+a,j+b):
                    dfs(i+a,j+b)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in path:
                    ans+=1
                    dfs(i,j)
        return ans
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        