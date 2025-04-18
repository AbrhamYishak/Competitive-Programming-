# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direct = [[0,1],[0,-1],[1,0],[-1,0]]
        que = deque()
        que.append([sr,sc])
        original = image[sr][sc]
        seen = set()
        def bound(i,j):
            if i < 0 or j < 0 or i >= len(image) or j >=len(image[0]) or image[i][j] != original:
                return False
            return True
        while que:
            for _ in range(len(que)):
                a = que.popleft()
                x,y = a
                seen.add((x,y))
                image[x][y] = color
                for i in direct:
                    a,b = i
                    if bound(x+a,y+b) and (x+a,y+b) not in seen:
                        que.append([x+a,y+b])
        return image
                