# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        direction = {'N':0,'E':1,'W':0,'S':0}
        done = [[0]*col for j in range(row)]
        ans = []
        while len(ans) < row*col:
            if direction['E'] == 1:
                direction['E'] = 0
                direction['S'] = 1
                for i in range(row):
                    found = False
                    for j in range(col):
                        if not done[i][j]:
                            ans.append(matrix[i][j])
                            done[i][j] = 1
                            found = True
                    if found:
                        break
            if direction['S'] == 1:
                direction['S'] = 0
                direction['W'] = 1
                for i in range(col-1,-1,-1):
                    found = False
                    for j in range(row):
                        if not done[j][i]:
                            ans.append(matrix[j][i])
                            done[j][i] = 1
                            found = True
                    if found:
                        break
            if direction['W'] == 1:
                direction['W'] = 0
                direction['N'] = 1 
                for i in range(row-1,-1,-1):
                    found = False
                    for j in range(col-1,-1,-1):
                        if not done[i][j]:
                            ans.append(matrix[i][j])
                            done[i][j] = 1
                            found = True
                    if found:
                        break           
            if direction['N'] == 1:
                direction['N'] = 0
                direction['E'] = 1
                for i in range(col):
                    found = False
                    for j in range(row-1,-1,-1):
                        if not done[j][i]:
                            ans.append(matrix[j][i])
                            done[j][i] = 1
                            found = True
                    if found:
                        break
        return ans       
        


        