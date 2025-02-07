# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans = [0,0]
        nums = Counter(nums)
        for i in nums:
            ans[0]+=(nums[i]//2)
            ans[1]+=nums[i]%2
        return ans        