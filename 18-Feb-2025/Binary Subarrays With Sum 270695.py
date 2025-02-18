# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def calculator(arr,k):
            start = 0
            n = len(arr)
            sum_arr = 0
            ans = 0
            for end in range(n):
                sum_arr+=arr[end]
                while sum_arr > k and start <= end :
                    sum_arr-=nums[start]
                    start+=1
                ans+=end-start+1
            return ans
        if goal:
            return calculator(nums,goal) - calculator(nums,goal-1)
        else:
            return calculator(nums,goal)