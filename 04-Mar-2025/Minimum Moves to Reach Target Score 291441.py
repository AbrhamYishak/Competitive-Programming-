# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while maxDoubles and target != 1:
            if target%2:
                ans+=1
                target-=1
            else:
                ans+=1
                target//=2
                maxDoubles-=1
        if target:
            ans+=target-1
        return ans