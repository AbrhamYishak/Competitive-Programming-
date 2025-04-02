# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        min_h = 0
        max_h = len(citations)
        def validate(h):
            count = 0
            for i in citations:
                if i >= h:
                    count+=1
            return count>=h
        while min_h <= max_h:
            mid = (min_h+max_h)//2
            if validate(mid):
                min_h = mid+1
            else:
                max_h = mid-1
        return max_h