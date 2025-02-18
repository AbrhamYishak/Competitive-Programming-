# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = {0:1}
        run_sum = 0
        ans = 0
        for i in nums:
            run_sum+=i
            if run_sum%k in d:
                ans+= d[run_sum%k]
            if run_sum%k not in d:
                d[run_sum%k] = 1
            else:
                d[run_sum%k] += 1
        return ans
        