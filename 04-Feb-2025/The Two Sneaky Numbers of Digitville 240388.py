# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        nums = Counter(nums)
        for i in nums:
            if nums[i] > 1:
                ans.append(i)
        return ans