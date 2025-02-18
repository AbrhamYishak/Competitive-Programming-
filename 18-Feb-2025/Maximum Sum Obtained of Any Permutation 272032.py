# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix = [0]*(len(nums)+1)
        for i in requests:
            start,end = i
            prefix[start]+=1
            prefix[end+1]-=1
        for j in range(1,len(prefix)):
            prefix[j] = prefix[j]+prefix[j-1]
        prefix.pop()
        nums.sort()
        prefix.sort()
        ans = 0
        for k in range(len(nums)):
            ans+=nums[k]*prefix[k]
        return (ans% (10**9 + 7))
