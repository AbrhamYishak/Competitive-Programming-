# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zeros = 0
        start = 0
        max_len = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                count_zeros+=1
            while count_zeros > k:
                if nums[start] == 0:
                    count_zeros-=1
                start+=1
            max_len = max(max_len,end-start+1)
        return max_len
            
        