# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        counter = [0,0]
        def divider(a):
            b = set(a)
            if len(a) == 2:
                if a[0].lower() in b and a[0].upper() in b:
                    return a
                return ""
            for i in range(len(a)):
                if a[i].lower() not in b or a[i].upper() not in b:
                    ans1 = divider(a[:i])
                    ans2 = divider(a[i+1:])
                    if len(ans1) >= len(ans2):
                        return ans1
                    else:
                        return ans2
            return a
        return divider(s)



