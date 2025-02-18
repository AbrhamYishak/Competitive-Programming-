# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [nums[-1]]
        for i in nums:
            prefix.append(i*prefix[-1])
        for j in range(len(nums)-2,-1,-1):
            suffix.append(suffix[-1]*nums[j])
        suffix.reverse()
        suffix.append(1)
        ans = [0]*len(nums)
        for i in range(len(nums)):
            ans[i] = prefix[i]*suffix[i+1]
        return ans
