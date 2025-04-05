# Problem: Subsets II - https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        a = []
        ans = [[]]
        def finder(i):
            if i == len(nums):
                return 
            a.append(nums[i])
            ans.append(a.copy())
            finder(i+1)
            while i + 1 < n and nums[i + 1] == nums[i]:
                i += 1 
            a.pop()
            finder(i+1)
        finder(0)
        return ans
        