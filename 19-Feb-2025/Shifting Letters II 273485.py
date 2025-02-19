# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        change = [0]*n
        for i in shifts:
            start,end,k = i
            if k:
                change[start]+=1
                if end+1 < n:
                    change[end+1] -= 1
            else:
                change[start]-=1
                if end+1 < n:
                    change[end+1] += 1
        for j in range(1,n):
            change[j] = change[j-1]+change[j]
        ans = ""
        for k in range(len(s)):
            ans+=chr((ord(s[k]) - 97 + change[k])%26 + 97)
        return ans
