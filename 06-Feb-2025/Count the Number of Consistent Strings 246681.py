# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(sorted(allowed))
        ans = 0
        for i in words:
            if allowed >= set(sorted(i)):
                ans+=1
        return ans        