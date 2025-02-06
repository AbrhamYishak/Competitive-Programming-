# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        possible = []
        for i in range(4):
            rotated = [[0]*n for x in range(n)]
            for j in range(n):
                for k in range(n):
                    rotated[n-k-1][j] = mat[j][k]
            possible.append(rotated)
            mat = rotated
        if target in possible:
            return True
        return False