# Problem: Majority Element II - https://leetcode.com/problems/majority-element-ii/?envType=daily-question&envId=2023-10-05

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)/3
        nums = Counter(nums)
        ans = []
        for i in nums:
            if nums[i] > l:
                ans.append(i)
        return ans