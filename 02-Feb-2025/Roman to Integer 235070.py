# Problem: Roman to Integer - https://leetcode.com/problems/roman-to-integer/?envType=problem-list-v2&envId=string

class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        for i in range(1,len(s)):
            if val[s[i-1]] < val[s[i]]:
                ans-= val[s[i-1]]
            else:
                ans+= val[s[i-1]]
        ans+=val[s[-1]]
        return ans
