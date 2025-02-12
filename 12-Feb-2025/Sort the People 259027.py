# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(1,n):
            j = i
            while heights[j-1] < heights[j] and j > 0:
                heights[j-1],heights[j] = heights[j],heights[j-1]
                names[j-1],names[j] = names[j],names[j-1]
                j-=1
        return names