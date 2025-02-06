# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            a = set()
            for j in range(9):
                if board[i][j]!="." and board[i][j] not in a:
                    a.add(board[i][j])
                elif board[i][j]!="." and board[i][j] in a:
                    return False
        for m in range(9):
            b = set()
            for n in range(9):
                if board[n][m]!="." and board[n][m] not in b:
                    b.add(board[n][m])
                elif board[n][m]!="." and board[n][m] in b:
                    return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                cube = set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l]!="." and board[k][l] not in cube:
                            cube.add(board[k][l])
                        elif board[k][l]!="." and board[k][l] in cube:
                            return False       
        return True
        