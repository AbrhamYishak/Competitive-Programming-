# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        dis = float("inf")
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                if nums[i]+nums[j]+nums[k] < target:
                    if abs(target-(nums[i]+nums[j]+nums[k])) < dis:
                        ans = nums[i]+nums[j]+nums[k]
                        dis = abs(target-(nums[i]+nums[j]+nums[k]))
                    j+=1
                elif nums[i]+nums[j]+nums[k] > target:
                    if abs(target-(nums[i]+nums[j]+nums[k])) < dis:
                        ans = nums[i]+nums[j]+nums[k]
                        dis = abs(target-(nums[i]+nums[j]+nums[k]))
                    k-=1
                else:
                    return(nums[i]+nums[j]+nums[k])     
        return ans         
        