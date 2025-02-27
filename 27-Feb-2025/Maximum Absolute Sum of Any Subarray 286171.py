# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum1 = float("-inf")
        previous_sum = 0
        current_sum = 0
        for i in nums:
            previous_sum = max(0,previous_sum)
            current_sum = previous_sum+i
            previous_sum = current_sum
            max_sum1 = max(max_sum1,current_sum)
        max_sum2 = float("inf")
        previous_sum = 0
        current_sum = 0
        for i in nums:
            previous_sum = min(0,previous_sum)
            current_sum = previous_sum+i
            previous_sum = current_sum
            max_sum2 = min(max_sum2,current_sum)
        return max(max_sum1,abs(max_sum2))