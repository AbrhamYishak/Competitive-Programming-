# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for mask in range(1<<n):
            subset = []
            for j in range(n):
                if (mask >> j) & 1:
                    subset.append(nums[j])
            ans.append(subset)
        return ans
        