# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        target = float("-inf")
        ans = 0
        for i in points:
            if i[0] > target:
                target = i[1]
                ans+=1
        return ans
        