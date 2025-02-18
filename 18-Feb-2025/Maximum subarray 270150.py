# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        previous_sum = 0
        current_sum = 0
        for i in nums:
            previous_sum = max(0,previous_sum)
            current_sum = previous_sum+i
            previous_sum = current_sum
            max_sum = max(max_sum,current_sum)
        return max_sum
        