# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        num = 0
        s = Counter(s)
        for i in s:
            num = s[i]
            break
        for j in s:
            if num!=s[j]:
                return False
        return True 
