# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        ans = [[0 for i in range(c)] for j in range(r)]
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        q = deque()
        visited = [[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    visited[i][j] = 1
                    q.append((i,j))
        level = 0
        while q:
            level+=1
            for i in range(len(q)):
                a,b = q.popleft()
                for j in direction:
                    a1,b1 = j
                    if -1<a+a1<r and -1<b+b1<c and mat[a+a1][b+b1]==0 and not visited[a+a1][b+b1]:
                        visited[a+a1][b+b1] = 1
                        q.append((a+a1,b+b1))
                    elif -1<a+a1<r and -1<b+b1<c and mat[a+a1][b+b1]!=0 and not visited[a+a1][b+b1]:
                        visited[a+a1][b+b1] = 1
                        ans[a+a1][b+b1] = level
                        q.append((a+a1,b+b1))
        return ans