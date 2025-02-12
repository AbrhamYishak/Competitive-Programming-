# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums.reverse()
        i = 0
        j = len(nums)-1
        a = k%len(nums)
        k = k%len(nums)
        while i < a:
            nums[i],nums[a-1] = nums[a-1],nums[i]
            i+=1
            a-=1
        while k < j:
            nums[k],nums[j] = nums[j],nums[k]
            k+=1
            j-=1
        """
        Do not return anything, modify nums in-place instead.
        """
        