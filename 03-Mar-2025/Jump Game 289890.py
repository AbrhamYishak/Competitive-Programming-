# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums)-1
        j = i-1
        while j > 0:
            if nums[j] >= i-j:
                i = j
                j = i-1
            else:
                j-=1
        if nums[j] >= i-j or len(nums) == 1:
            return True
        return False                       

