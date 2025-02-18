# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:   
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        run_sum = 0
        ans = 0
        for i in nums:
            run_sum+=i
            if run_sum-k in d:
                ans+=d[run_sum-k]
            if run_sum not in d:
                d[run_sum] = 1
            else:
                d[run_sum] += 1
        return ans
