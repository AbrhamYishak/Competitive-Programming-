# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        col = len(self.matrix[0])
        row = len(self.matrix)
        self.mat = [[0]*(col+1) for x in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                self.mat[i][j] = self.mat[i-1][j] + self.mat[i][j-1] + self.matrix[i-1][j-1] - self.mat[i-1][j-1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.mat[row2+1][col2+1] - self.mat[row2+1][col1] - self.mat[row1][col2+1] + self.mat[row1][col1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)