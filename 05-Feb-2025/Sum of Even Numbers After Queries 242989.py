# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        sum_even = sum([k for k in nums if k%2==0])
        for i in queries:
            val,ind = i
            if (val%2==0 and nums[ind]%2 == 0) or (val%2!=0 and nums[ind]%2 != 0):
                if nums[ind]%2 == 0:
                    sum_even+=val
                else:
                    sum_even+=nums[ind]+val
                nums[ind] = nums[ind]+val
            else:
                if nums[ind]%2 == 0:
                    sum_even-=nums[ind]
                nums[ind] = nums[ind]+val
            ans.append(sum_even)
        return ans
        