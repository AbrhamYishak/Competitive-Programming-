# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        b = []
        n = len(board)
        turn = True
        for i in range(n-1,-1,-1):
            if turn:
                b.extend(board[i])
                turn = not turn
            else:
                b.extend(board[i][::-1])
                turn = not turn
        q = deque()
        q.append(1)
        visited = {1}
        level = 0
        while(q):
            level+=1
            for i in range(len(q)):
                a = q.popleft()
                for j in range(1,7):
                    if a+j not in visited:
                        if a+j == n*n:
                            return level
                        if b[a+j-1] == -1:
                            visited.add(a+j)
                            q.append(a+j)
                        else:
                            if b[a+j-1] ==  n*n:
                                return level
                            visited.add(a+j)
                            q.append(b[a+j-1])
        return -1

        
            
