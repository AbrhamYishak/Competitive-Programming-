# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution(object):
    def largestLocal(self, grid):
        row = len(grid)
        col = len(grid[0])
        ans = [[0]*(col-2) for r in range(row-2)]
        for i in range(1,row-1):
            for j in range(1,col-1):
                val = float("-inf")
                for k in range(i-1,min(row,i+2)):
                    for l in range(j-1,min(col,j+2)):
                        val = max(val,grid[k][l])
                ans[i-1][j-1] = val
        return ans

        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        