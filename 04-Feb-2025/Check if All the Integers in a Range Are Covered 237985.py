# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        a = set()
        b = set()
        for i in ranges:
            a.update(range(i[0],i[1]+1))
        b.update(range(left,right+1))
        if b <= a:
            return True
        return False
        
        
        