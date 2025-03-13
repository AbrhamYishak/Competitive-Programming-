# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [num for num in range(1,n+1)]
        def deleter(players,index):
            if len(players) > 1:
                index = (index + k-1)%(len(players))
                a = players.pop(index) 
                return deleter(players,index)
            else:
                return players[0]
        return deleter(players,0)

        