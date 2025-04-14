# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution(object):
    def maxAreaOfIsland(self, grid):
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def validate(i,j):
            n = len(grid)
            m = len(grid[0])
            if i>=n or j>=m or i < 0 or j < 0 or not grid[i][j]:
                return False
            else:
                return True
        seen = set()
        def dfs(i,j):
            area = 1
            seen.add((i,j))
            for k in directions:
                a,b = k
                if validate(i+a,j+b) and (i+a,j+b) not in seen:
                    area+=dfs(i+a,j+b)
                else:
                    area+=0
            return area
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i,j) not in seen:
                    ans = max(ans,dfs(i,j))
        return ans
            
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        