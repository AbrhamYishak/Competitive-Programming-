# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums)-1
        num = {}
        for ind,val in enumerate(nums):
            if val not in num:
                num[val] = [ind]
            else:
                num[val].append(ind)
        nums.sort()
        while i < j:
            if nums[i]+nums[j] < target:
                i+=1
            elif nums[i]+nums[j] > target:
                j-=1
            else:
                if num[nums[i]] !=num[nums[j]]:
                    return [num[nums[i]][0],num[nums[j]][0]]
                else:
                    return [num[nums[i]][0],num[nums[j]][1]]
