# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n-2):
            j = i+1
            k = n-1
            if i > 0 and nums[i] == nums[i-1] :
                continue
            while j < k:
                if nums[i]+nums[j]+nums[k] < 0:
                    j+=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
        return(ans)

                