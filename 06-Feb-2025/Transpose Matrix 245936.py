# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        ans = [[0]*row for y in range(col)]
        for i in range(row):
            for j in range(col):
                ans[j][i] = matrix[i][j]
        return ans
        