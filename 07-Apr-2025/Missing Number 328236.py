# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = max(nums)+1
        for _ in range(max_num+1):
            if _ not in nums:
                return _
        