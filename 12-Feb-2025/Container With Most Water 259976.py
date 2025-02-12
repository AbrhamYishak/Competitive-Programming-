# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0 
        j = len(height)-1
        max_area = 0
        while i < j:
            if height[i] < height[j]:
                max_area = max(max_area,height[i]*(j-i))
                i+=1
            else:
                max_area = max(max_area,height[j]*(j-i))
                j-=1
        return max_area
