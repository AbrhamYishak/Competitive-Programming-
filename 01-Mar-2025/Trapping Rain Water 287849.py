# Problem: Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        count = 0
        max_height_left = 0
        max_height_right = 0
        while i < j:
            if max_height_left > height[i]:
                count+= max_height_left - height[i]
            if max_height_right > height[j]:
                count+= max_height_right - height[j]
            max_height_left = max(max_height_left,height[i])
            max_height_right = max(max_height_right,height[j])
            if max_height_left <= max_height_right:
                i+=1
            else:
                j-=1
        return count

