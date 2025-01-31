# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution(object):
    def separateDigits(self, nums):
        ans = []
        for i in nums:
            for j in str(i):
                ans.append(int(j))
        return ans
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        