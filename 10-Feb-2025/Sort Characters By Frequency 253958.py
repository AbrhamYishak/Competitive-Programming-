# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        ans = []
        s = Counter(s)
        s = dict(sorted(s.items(), key = lambda x : x[1] ,reverse = True))
        for i in s:
            for j in range(s[i]):
                ans.append(i)
        return "".join(ans)
        