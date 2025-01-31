# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution(object):
    def constructTransformedArray(self, nums):
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = nums[(i+nums[i])%len(nums)]
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        