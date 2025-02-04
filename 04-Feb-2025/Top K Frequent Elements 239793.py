# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

from collections import *
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        l = list(nums.keys())
        l.sort(key = lambda x: nums[x],reverse = True)
        return l[:k]