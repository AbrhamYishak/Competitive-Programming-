# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = [0,0]
        ans = 0
        for i in s:
            if i == 'R':
                balance[1]+=1
            else:
                balance[0]+=1
            if balance[0] == balance[1]:
                ans+=1
        return ans
