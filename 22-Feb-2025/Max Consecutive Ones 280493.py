# Problem: Max Consecutive Ones - https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        end = 0
        count = 0
        max_count = 0
        while end < len(nums):
            if nums[end] == 1:
                count += 1
            elif nums[end] != 1:
                count = 0
            max_count = max(max_count,count)
            end += 1
        return max_count        


        