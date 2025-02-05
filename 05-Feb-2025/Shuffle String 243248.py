# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a = [" "]*len(s)
        for i in range(len(indices)):
            a[indices[i]] = s[i]
        return "".join(a)
        