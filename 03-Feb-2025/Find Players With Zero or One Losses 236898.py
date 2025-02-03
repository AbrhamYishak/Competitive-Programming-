# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        record = {}
        for i in matches:
            w,l = i
            record[w] = 0
            record[l] = 0
        for i in matches:
            w,l = i
            record[l] += 1
        ans = [sorted([j for j in record if record[j] == 0]), sorted([k for k in record if record[k] == 1])]
        return ans        