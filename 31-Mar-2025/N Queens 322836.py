# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_used = [False]*n
        pos_dia = {}
        neg_dia = {}
        for i in range(n):
            for j in range(n):
                pos_dia[i+j] = False
                neg_dia[i-j] = False
        soln = []
        a = []
        def solver(r):
            if r == n:
                soln.append(a.copy())
            for i in range(n):
                if not col_used[i] and not pos_dia[r+i] and not neg_dia[r-i]:
                    a.append([r,i])
                    col_used[i] = True
                    pos_dia[r+i] = True
                    neg_dia[r-i] = True
                    solver(r+1)
                    a.pop()
                    col_used[i] = False
                    pos_dia[r+i] = False
                    neg_dia[r-i] = False
                else:
                    continue
        solver(0)
        final = [["." for i in range(n)] for j in range(n)]
        ans = []
        for k in soln:
            for i in range(n):
                for j in range(n):
                    if [i,j] in k:
                        final[i][j] = 'Q'
            final = ["".join(x) for x in final]
            ans.append(final)
            final = [["." for i in range(n)] for j in range(n)]
        return ans



        