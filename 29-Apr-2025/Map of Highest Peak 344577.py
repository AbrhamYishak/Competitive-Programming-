# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n,m = len(isWater),len(isWater[0])
        solution = [[-1 for _ in range(m)] for _ in range(n)]
        current_level = []
        level = 0
        for r in range(n):
            for c in range(m):
                if isWater[r][c]:
                    current_level.append((r,c))
                    solution[r][c] = level
        while current_level:
            next_level = []
            level += 1
            for x,y in current_level:
                for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nx,ny = x+dx,y+dy
                    if -1 < nx < n and -1 < ny < m:
                        if solution[nx][ny] == -1:
                            next_level.append((nx,ny))
                            solution[nx][ny] = level
            current_level = next_level[:]
        return solution