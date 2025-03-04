# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = [0,0]
        ans = []
        for i in s:
            if i == '0':
                count[0]+=1
            else:
                count[1]+=1
        for i in range(count[1]-1):
            ans.append('1')
        for j in range(count[0]):
            ans.append('0')
        if count[1] > 0:
            ans.append('1')
        return "".join(ans)
        