# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])
        ans = []
        flip = 1
        i = 0
        j = 0
        k = 0
        if row > 0 and col > 0:
            length = row+col-1
        else:
            length = row+col
        while k < length:
            a = i
            b = j
            arr = []
            while a <= row-1 and b >= 0:
                arr.append(mat[a][b])
                a+=1
                b-=1
            if flip:
                for t in arr[::-1]:
                    ans.append(t)
                if j < col-1:
                    j+=1
                else:
                    i+=1
                flip = 0
                k+=1
            else:
                for t in arr:
                    ans.append(t)
                if j < col-1:
                    j+=1
                else:
                    i+=1
                flip = 1
                k+=1
        return ans
        
        
            
