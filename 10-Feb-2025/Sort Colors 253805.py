# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        n = len(nums)
        while i < n:
            for j in range(1,n-i):
                if nums[j-1] > nums[j]:
                    nums[j-1],nums[j] = nums[j],nums[j-1]
            i+=1
        """
        Do not return anything, modify nums in-place instead.
        """
        