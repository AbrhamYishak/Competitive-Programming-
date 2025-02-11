# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_val = max(nums)
        min_val = min(nums)
        offset = abs(min(0,min_val))
        range_val = max_val+abs(min_val)+1
        count = [0]*(range_val)
        for i in nums:
            count[i+offset]+=1
        ans = []
        for j in range(range_val):
            for k in range(count[j]): 
                ans.append(j-offset)
        return ans
        