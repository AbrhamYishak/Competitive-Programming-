# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque()
        visited = [[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    q.append((i,j))
        while q:
            for i in range(len(q)):
                a,b = q.popleft()
                for j in direction:
                    a1,b1 = j
                    if -1<a+a1<r and -1<b+b1<c and not visited[a+a1][b+b1]:
                        visited[a+a1][b+b1] = 1
                        mat[a+a1][b+b1] = mat[a][b]+1
                        q.append((a+a1,b+b1))
        return mat