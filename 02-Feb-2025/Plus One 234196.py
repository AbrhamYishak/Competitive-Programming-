# Problem: Plus One - https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:
            num+=str(i)
        num = str(int(num)+1)
        return [int(a) for a in num]       