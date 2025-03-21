# Problem: Combination Sum II - https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        l = candidates
        l.sort()
        n = len(l)
        ans = []
        a = []
        def backtracker(i,answer):
            if answer > target or i >= n:
                return
            a.append(l[i])
            answer+=l[i]
            if answer == target:
                ans.append(a.copy())
            backtracker(i+1,answer)
            answer-=l[i]
            a.pop()
            while i+1 < n and l[i] == l[i+1]:
                i+=1
            backtracker(i+1,answer)
        backtracker(0,0)
        return ans