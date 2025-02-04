# Problem: Contains Duplicate - https://leetcode.com/problems/contains-duplicate/description/

from collections import *
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(Counter(nums))
        