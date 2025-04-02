# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_1 = []
        for i in matrix:
            col_1.append(i[0])
        a = bisect_left(col_1,target)
        if a < len(col_1) and col_1[a] == target:
            return True
        elif a == 0:
            return False
        else:
            c = matrix[a-1]
            pos =  bisect_left(c,target)
            if pos < len(c) and c[pos] == target:
                return True
            else:
                return False 

        